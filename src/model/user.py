from datetime import datetime

from psycopg2 import extras

from src.util import util_get_config, pg_list, pg_create, pg_get, pg_delete, pg_get_connection, pg_return_connection, \
    pg_update, pg_get_by_ids, s3_get_profile_url


def user_list(fltr):
    businessid = fltr.get('businessId')
    allow_facilieties = fltr.get('allow_facilieties', {})
    if len(allow_facilieties) > 0:  # not admin
        if businessid is not None and businessid not in allow_facilieties:
            raise AssertionError('Insufficient privileges')

    if businessid is not None:
        res = _user_list_with_components([businessid])
    elif len(allow_facilieties) != 0:
        res = _user_list_with_components(allow_facilieties)
    else:
        return pg_list(util_get_config(), 'users')

    role = fltr.get('role', 0)
    if role > 0:
        res = filter(lambda v: role in v['roles'], res)
    status = fltr.get('status', 0)
    if status > 0:
        res = filter(lambda v: status == (v['activationstatus'] if v['activationstatus'] != None else 1), res)

    return res


def user_like(fltr):
    sql = 'SELECT * FROM users WHERE'
    where = ''
    for k, v in fltr.items():
        joinwhere = ' AND ' if len(where) > 0 else ' '
        if k == 'likeFirstName':
            where = joinwhere.join((where, 'first_name like \'{}\''.format(v)))
        elif k == 'likeLastName':
            where = joinwhere.join((where, 'last_name like \'{}\''.format(v)))
        elif k == 'likeSSN':
            where = joinwhere.join((where, 'ssn like \'{}\''.format(v)))
        elif k == 'dob':
            fmt = '%b %d %Y'
            dob = datetime.strptime(v[4:15], fmt)
            where = joinwhere.join((where, 'dob = \'{}\''.format(dob)))
    sql = ' '.join((sql, where))
    con = pg_get_connection(util_get_config()['pg'])
    cur = con.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute(sql)
    records = cur.fetchall()
    cur.close()
    pg_return_connection(con)
    return records


def user_get(recid):
    doc = pg_get(util_get_config(), 'users', recid)
    if doc is not None:
        doc['avatar'] = s3_get_profile_url(doc['id'])
    return doc


def user_get_by_phone(phone_number):
    return pg_get(util_get_config(), 'users', phone_number, 'phone_number')


def user_get_by_ids(recid):
    return pg_get_by_ids(util_get_config(), 'users', recid)


def user_create(doc):
    doc.pop('id', None)
    recid = pg_create(util_get_config(), 'users', doc)
    return pg_get(util_get_config(), 'users', recid)


def user_delete(recid):
    return pg_delete(util_get_config(), 'users', recid)


def user_update(recid, doc):
    doc.pop('id', None)
    doc.pop('username', None)
    pg_update(util_get_config(), 'users', recid, doc)
    return pg_get(util_get_config(), 'users', recid)


def _user_list_with_components(allow_facilieties):
    sql = """
    SELECT uf.facilityid, u.*, ufa.status activationstatus\
    FROM users u\
    RIGHT JOIN userfacility uf ON(u.id=uf.userid)\
    LEFT JOIN facility f ON (f.id=uf.facilityid)\
    LEFT JOIN userfacilitytestaccess ufa ON (u.id=ufa.userid)\
    WHERE f.id IN ({})\
    """.format(','.join(str(i) for i in allow_facilieties))

    con = pg_get_connection(util_get_config()['pg'])
    cur = con.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute(sql)
    res = [i for i in cur.fetchall()]
    cur.close()
    pg_return_connection(con)
    return res
