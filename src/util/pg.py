from psycopg2 import pool, errors
from psycopg2.extensions import AsIs
from psycopg2 import pool, extras
import psycopg2
import logging

from .appexcept import AppLogicalError

_pg_pool = None


def _pg_connect(pgcnf):
    global _pg_pool
    _pg_pool = psycopg2.pool.ThreadedConnectionPool(1, 1000, user=pgcnf['user'],
                                                    password=pgcnf['pwd'],
                                                    host=pgcnf['host'],
                                                    port=pgcnf['port'],
                                                    database=pgcnf['db'])


def pg_get_connection(pgcnf):
    global _pg_pool
    if not _pg_pool:
        _pg_connect(pgcnf)
    try:
        conn = _pg_pool.getconn()
        if not conn:
            raise Exception('PG connection not created')
    except Exception as ex:
        logging.getLogger(__name__).exception(ex)
        raise AppLogicalError(-1, 'Cannot connect to database.')
    return conn


def pg_return_connection(con):
    global _pg_pool
    _pg_pool.putconn(con)


def pg_reset_connection():
    global _pg_pool
    _pg_pool = None


def pg_intarray_to_in(ints):
    return ','.join([str(i) for i in ints])


def pg_insert_doc(con, table, doc, do_commit):
    columns = doc.keys()
    values = [doc[column] for column in columns]
    sql = 'INSERT INTO {0} (%s) VALUES %s RETURNING id'.format(table)
    cur = con.cursor()
    stmt = cur.mogrify(sql, (AsIs(','.join(columns)), tuple(values)))
    cur.execute(stmt)
    recid = cur.fetchone()[0]
    if do_commit:
        con.commit()
    return recid


def pg_list(cnf, table):
    con = pg_get_connection(cnf['pg'])
    cur = con.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute('SELECT * FROM {}'.format(table))
    data = [i for i in cur.fetchall()]
    cur.close()
    pg_return_connection(con)
    return data


def pg_get(cnf, table, recid, idfield='id'):
    con = pg_get_connection(cnf['pg'])
    cur = con.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute('SELECT * FROM {} WHERE {}=%s'.format(table, idfield), (recid,))
    record = cur.fetchone()
    cur.close()
    pg_return_connection(con)
    return record


def pg_get_by_ids(cnf, table, ids, idfield='id'):
    con = pg_get_connection(cnf['pg'])
    cur = con.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute('SELECT * FROM {} WHERE {} IN ({})'.format(table, idfield, pg_iids2in(ids)))
    record = cur.fetchall()
    cur.close()
    pg_return_connection(con)
    return record


def pg_get_in(cnf, table, recids, idfield='id'):
    sql = 'SELECT * FROM {} WHERE {} IN ({})'.format(table, idfield, pg_intarray_to_in(recids))
    con = pg_get_connection(cnf['pg'])
    cur = con.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute(sql)
    data = [i for i in cur.fetchall()]
    cur.close()
    pg_return_connection(con)
    return data


def pg_update(cnf, table, tid, doc, idfield='id'):
    columns = doc.keys()
    values = [doc[column] for column in columns]
    set_vals = ','.join([i + '=%s' for i in columns])
    sql = 'UPDATE {0} SET {1} WHERE {3}={2} RETURNING {3}'.format(table, set_vals, tid, idfield)
    con = pg_get_connection(cnf['pg'])
    cur = con.cursor()
    stmt = cur.mogrify(sql, (values))
    cur.execute(stmt)
    rc = cur.fetchone()
    cur.close()
    con.commit()
    pg_return_connection(con)
    if rc is None:
        raise AppLogicalError(-1, 'Failed to update {}/{}'.format(table, tid))
    return rc


def pg_create(cnf, table, doc, idfield='id'):
    columns = doc.keys()
    values = [doc[column] for column in columns]
    sql = 'INSERT INTO {0} (%s) VALUES %s RETURNING {1}'.format(table, idfield)
    con = pg_get_connection(cnf['pg'])
    cur = con.cursor()
    stmt = cur.mogrify(sql, (AsIs(','.join(columns)), tuple(values)))
    try:
        cur.execute(stmt)
        recid = cur.fetchone()[0]
        con.commit()
    except errors.UniqueViolation as ex:
        raise AssertionError('Record in {} already exist'.format(table))
    finally:
        pg_return_connection(con)
    return recid


def pg_count_by_field(cnf, table, recid, idfield='id'):
    con = pg_get_connection(cnf['pg'])
    cur = con.cursor()
    cur.execute('SELECT COUNT(*) FROM {} WHERE {}=%s'.format(table, idfield), (recid,))
    count = cur.fetchone()
    cur.close()
    pg_return_connection(con)
    return count[0]


def pg_delete(cnf, table, id, idfield='id'):
    con = pg_get_connection(cnf['pg'])
    cur = con.cursor()
    cur.execute('DELETE FROM {} WHERE {}=%s'.format(table, idfield), (id,))
    con.commit()
    pg_return_connection(con)
    return id


def pg_get_val(data, tag, default):
    res = data.get(tag, None)
    if res == None:
        res = default
    return res


def pg_tbl_count(cnf, tbl):
    con = pg_get_connection(cnf['pg'])
    cur = con.cursor()
    cur.execute('SELECT COUNT(*) from {}.{}'.format(cnf['pg']['schema'], tbl))
    res = cur.fetchone()
    cur.close()
    pg_return_connection(con)
    return res[0]


def pg_list_by(cnf, table, value, field, order_fld=None):
    con = pg_get_connection(cnf['pg'])
    cur = con.cursor(cursor_factory=extras.RealDictCursor)
    sql = 'SELECT * FROM {0} WHERE {1}={2}'.format(table, field, value)
    if order_fld is not None:
        sql = ' '.join((sql, 'ORDER BY {} DESC'.format(order_fld)))
    cur.execute(sql)
    data = [i for i in cur.fetchall()]
    cur.close()
    pg_return_connection(con)
    return data


def pg_get_last(cnf, table, value, idfield='id'):
    con = pg_get_connection(cnf['pg'])
    cur = con.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute('SELECT * FROM {} WHERE {}=%s ORDER BY id DESC LIMIT 1'.format(table, idfield), (value,))
    record = cur.fetchone()
    cur.close()
    pg_return_connection(con)
    return record


def pg_nextval(cnf, seqname):
    con = pg_get_connection(cnf['pg'])
    cur = con.cursor()
    cur.execute("select nextval('{}')".format(seqname))
    record = cur.fetchone()
    cur.close()
    pg_return_connection(con)
    return record


def pg_iids2in(ids):
    return ','.join(str(i) for i in ids)
