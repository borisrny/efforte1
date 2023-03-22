from psycopg2 import extras

from src.util import util_get_config, pg_list, pg_create, pg_get, pg_list_by, pg_get_last, pg_return_connection, \
    fmt_date
from src.util import pg_get_connection, s3_get_covidtest_url, s3_get_requisition_url, pg_iids2in, pg_update


def testresult_list(test_type, fltr=None):
    return pg_list(util_get_config(), test_type)


def testresult_get(test_type, recid):
    return pg_get(util_get_config(), test_type, recid)


def testresult_create(test_type, userid, post_userid, doc):
    doc['userid'] = userid
    doc['postuser'] = post_userid
    u_id = pg_create(util_get_config(), test_type, doc)
    doc = pg_get(util_get_config(), test_type, u_id)
    if test_type == 'covidtest':
        doc['date_of_test'] = fmt_date(doc['date_of_test'])
    return doc


def testresult_update(test_id, test_type, userid, post_userid, doc):
    doc['userid'] = userid
    doc['postuser'] = post_userid
    u_id = pg_update(util_get_config(), test_type, test_id, doc)
    return pg_get(util_get_config(), test_type, u_id)


def testresult_get_byuser(test_type, userid):
    return pg_list_by(util_get_config(), test_type, userid, 'userid', 'id')


def testresult_last_byuser(test_type, userid):
    doc = pg_get_last(util_get_config(), test_type, userid, 'userid')
    if doc is not None and test_type == 'covidtest':
        doc['pictureURL'] = s3_get_covidtest_url(doc['id'])
        doc['requisitionTestURL'] = s3_get_requisition_url(doc['id'])
        # doc['date_of_test'] = fmt_date(doc['date_of_test'])
    return doc


def testresult_last_byuser_ids(test_type, ids):
    sql = 'SELECT * FROM {0} WHERE id IN ' \
          '(SELECT MAX(id) FROM {0} WHERE userid IN ({1}) GROUP BY userid)'.format(test_type, pg_iids2in(ids))
    con = pg_get_connection(util_get_config()['pg'])
    cur = con.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute(sql)
    records = cur.fetchall()
    cur.close()
    pg_return_connection(con)
    return records
