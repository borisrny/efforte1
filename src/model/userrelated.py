from datetime import timedelta

from src.model import user_create, user_get, user_delete, user_update, testresult_last_byuser, testresult_create, \
    testresult_get_byuser, fmt_date
from src.util import pg_get_connection, pg_return_connection, util_get_config, extras, pg_create, s3_get_profile_url


def userrelated_is_parent(parentid, userid):
    sql = 'SELECT EXISTS(SELECT 1 FROM userrelated WHERE parentid=%s AND userid=%s)'
    con = pg_get_connection(util_get_config()['pg'])
    cur = con.cursor()
    cur.execute(sql, (parentid, userid))
    res = cur.fetchone()
    cur.close()
    pg_return_connection(con)
    return res


def userrelated_list(parentid):
    """
    UsersSelfRelated.get - users related to parent
    :param parentid:
    :return:
    """
    sql = 'SELECT u.*, r.relationreason FROM users u, userrelated r WHERE r.parentid=%s and u.id=r.userid'
    con = pg_get_connection(util_get_config()['pg'])
    cur = con.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute(sql, (parentid,))
    data = [i for i in cur.fetchall()]
    cur.close()
    pg_return_connection(con)
    for i in data:
        i['relationReason'] = i.pop('relationreason')
        i['avatar'] = s3_get_profile_url(i['id'])
    return data


def userrelated_create(parentid, doc):
    """
    Add user related to parent
    :param parentid:
    :param doc:
    :return:
    """
    relation_reason = doc.pop('relationReason')
    doc = user_create(doc)
    pg_create(util_get_config(), 'userrelated',
              {'parentid': parentid, 'userid': doc['id'], 'relationreason': relation_reason},
              parentid)
    doc['relationReason'] = relation_reason
    return doc


def userrelated_update(parentid, recid, doc):
    if not userrelated_is_parent(parentid, recid):
        raise AssertionError('User {} not parent of {}'.format(parentid, recid))
    relation_reason = doc.pop('relationReason', None)
    return user_update(recid, doc)


def userrelated_get(parentid, recid):
    """
    get user (related to parent)
    :param parentid:
    :param recid:
    :return:
    """
    if not userrelated_is_parent(parentid, recid):
        raise AssertionError('User {} not parent of {}'.format(parentid, recid))
    sql = 'SELECT u.*, r.relationreason FROM users u, userrelated r WHERE r.parentid=%s and u.id=r.userid AND u.id=%s'
    con = pg_get_connection(util_get_config()['pg'])
    cur = con.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute(sql, (parentid, recid))
    doc = cur.fetchone()
    cur.close()
    pg_return_connection(con)
    if doc is not None:
        doc['avatar'] = s3_get_profile_url(doc['id'])
    return doc


def userrelated_delete(parentid, recid):
    if not userrelated_is_parent(parentid, recid):
        raise AssertionError('User {} not parent of {}'.format(parentid, recid))
    return user_delete(recid)


########    TEST RESULTS    ########


def userrelated_testresult_get(parentid, test_type, recid):
    if not userrelated_is_parent(parentid, recid):
        raise AssertionError('User {} not parent of {}'.format(parentid, recid))
    return testresult_last_byuser(test_type, recid)


def userrelated_testresult_list(parentid, test_type, recid):
    if not userrelated_is_parent(parentid, recid):
        raise AssertionError('User {} not parent of {}'.format(parentid, recid))
    return testresult_get_byuser(test_type, recid)


def userrelated_testresult_create(parentid, test_type, userid, poist_userid, doc):
    if not userrelated_is_parent(parentid, userid):
        raise AssertionError('User {} not parent of {}'.format(parentid, userid))
    return testresult_create(test_type, userid, parentid, doc)


def user_get_testsummaries(parentid):
    ret = []
    ids = [i['id'] for i in userrelated_list(parentid)]
    ids.append(parentid)
    for i in ids:
        cov_dt_str = cov_exp_str = quest_dt_str = quest_exp_str = None

        cov = testresult_last_byuser('covidtest', i)
        if cov:
            cov_dt = cov['date_of_test']
            cov_exp = cov_dt + timedelta(weeks=2)
            cov_dt_str = fmt_date(cov_dt)
            cov_exp_str = fmt_date(cov_exp)

        quest = testresult_last_byuser('questionnaire', i)
        if quest:
            quest_dt = quest['posttimestamp']
            quest_exp = quest_dt + timedelta(hours=24)
            quest_dt_str = fmt_date(quest_dt)
            quest_exp_str = fmt_date(quest_exp)

        ret.append({
            'userId': i,
            'questionnairyDate': quest_dt_str,
            'questionnairyExpDate': quest_exp_str,
            'covidtestDate': cov_dt_str,
            'covidtestExpDate': cov_exp_str
        })
    return ret
