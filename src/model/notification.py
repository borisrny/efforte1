from psycopg2 import extras

from src.util import util_get_config, pg_create, pg_get, pg_delete, pg_update, pg_get_connection, \
    pg_return_connection


def notification_list(fltr=None):
    con = pg_get_connection(util_get_config()['pg'])
    cur = con.cursor(cursor_factory=extras.RealDictCursor)
    sql = 'SELECT n.*, CASE WHEN n.postfacility IS NULL THEN \'PCI\' ELSE f.name END AS postername ' \
          'FROM notification n ' \
          'LEFT JOIN facility f ON f.id=n.postfacility ' \
          'ORDER BY postdate DESC'
    cur.execute(sql)
    data = [i for i in cur.fetchall()]
    cur.close()
    pg_return_connection(con)
    return data


def notification_get(recid):
    return pg_get(util_get_config(), 'notification', recid, ord)


def notification_create(user_id, facility_id, doc):
    doc['postuser'] = user_id
    doc['postfacility'] = facility_id
    u_id = pg_create(util_get_config(), 'notification', doc)
    return pg_get(util_get_config(), 'notification', u_id)


def notification_delete(recid):
    return pg_delete(util_get_config(), 'notification', recid)


def notification_update(recid, doc):
    doc.pop('id', None)
    return pg_update(util_get_config(), 'notification', recid, doc)
