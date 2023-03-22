import logging
from datetime import datetime, timedelta, timezone

from psycopg2 import extras

from src.model import user_get_by_ids, testresult_last_byuser_ids, bussiness_testrequirements_get, user_get
from src.util import pg_get_connection, pg_return_connection, util_get_config, pg_create, s3_get_covidtest_url, \
    s3_get_profile_url, util_get_nulloverride, pg_nextval


def facilityqueue_get(f_id: int):
    requirements = bussiness_testrequirements_get(f_id)

    from_time = datetime.now() - timedelta(hours=12)
    sql = "SELECT * FROM customerqueu WHERE facilityid=%s AND time_requested >= \'{}\' ORDER BY time_requested ASC" \
        .format(from_time)
    con = pg_get_connection(util_get_config()['pg'])
    cur = con.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute(sql, (f_id,))
    facility_queue_users = {i['userid']: {'queueItem': i} for i in cur.fetchall()}
    cur.close()
    pg_return_connection(con)
    ids = list(facility_queue_users.keys())
    if len(ids) == 0:
        return []
    for u in user_get_by_ids(ids):
        u['avatar'] = s3_get_profile_url(u['id'])
        facility_queue_users[u['id']]['user'] = u
    for t in testresult_last_byuser_ids('covidtest', ids):
        t['pictureURL'] = s3_get_covidtest_url(t['id'])
        facility_queue_users[t['userid']]['covidTest'] = t
    for t in testresult_last_byuser_ids('questionnaire', ids):
        t['postdate'] = t['posttimestamp']
        facility_queue_users[t['userid']]['questionnaire'] = t
    for t in testresult_last_byuser_ids('vitals', ids):
        t['postdate'] = t['posttimestamp']
        facility_queue_users[t['userid']]['vitals'] = t
    res = list(facility_queue_users.values())
    for u in res:
        u['requirementsMatch'] = facilityqueue_pass(requirements, u)
    return res


def facilityqueue_add(f_id: int, u_id: int, related):
    logging.getLogger(__name__).info('Facility: {}, User: {}, related: {}'.format(f_id, u_id, related))
    grouping = None
    if len(related) > 0:
        grouping = pg_nextval(util_get_config(), 'customerqueue_related_seq')

    doc = {
        'userid': u_id, 'facilityid': f_id,
        'time_requested': datetime.utcnow(),
        'related': grouping
    }
    pg_create(util_get_config(), 'customerqueu', doc, 'facilityid')
    requirements = bussiness_testrequirements_get(f_id)
    u = user_get(u_id)
    res = [{'id': u_id, 'status': facilityqueue_pass(requirements, u)}]
    for r_id in related:
        r_user = user_get(r_id)
        doc = {
            'userid': r_id, 'facilityid': f_id,
            'time_requested': datetime.utcnow(),
            'related': grouping
        }
        pg_create(util_get_config(), 'customerqueu', doc, 'facilityid')
        res.append({'id': r_id, 'status': facilityqueue_pass(requirements, r_user)})
    return res


def facilityqueue_grant(f_id: int, u_id: int, grant: bool):
    stat = 2 if grant else 3
    sql = 'UPDATE customerqueu SET access_status={}, time_in=\'{}\' WHERE facilityid=%s AND userid=%s' \
        .format(stat, datetime.utcnow())
    con = pg_get_connection(util_get_config()['pg'])
    cur = con.cursor()
    cur.execute(sql, (f_id, u_id))
    cur.close()
    con.commit()
    pg_return_connection(con)


def facilityqueue_pass(requirements, user):
    if user is None:
        return False
    # test COVID
    covid = requirements['covidTest']
    curent_time = datetime.now(timezone.utc)
    # def _test_bool(tag)
    if covid is not None:
        u_covid = user.get('covidTest')
        if not u_covid:
            return False
        test_date = u_covid['date_of_test']
        if test_date is None:
            return covid['valid_days'] == 0
        test_age = (curent_time.date() - test_date).days
        if test_age > covid['valid_days']:
            return False
        if not _facilityqueue_test_bools(u_covid, covid):
            return False
    # test Questionnarie
    ques = requirements.get('questionnaireRequirements', {})
    if ques is not None:
        u_ques = user.get('questionnaire')
        if not u_ques:
            return False
        test_age = (curent_time - u_ques['posttimestamp']).seconds / 3600
        if test_age > ques['valid_hours']:
            return False
        if not _facilityqueue_test_bools(u_ques, ques):
            return False
    # test VITALS
    vitals = requirements.get('vitalRequirements', {})
    if vitals is not None:
        u_vitals = user.get('vitals')
        if not u_vitals:
            return False
        test_age = (curent_time - u_vitals['posttimestamp']).seconds / 3600
        if test_age > vitals['valid_hours']:
            return False
        if not _facilityqueue_test_vitals(u_vitals, vitals):
            return False
    return True


def _facilityqueue_test_vitals(user_test, req):
    if util_get_nulloverride(user_test, 'temp', 100) > req['temp'] or \
            util_get_nulloverride(user_test, 'percent', 100) < req['percent']:
        return False
    bp_str = util_get_nulloverride(user_test, 'bp', '0/0').split('/')
    diastolic = float(bp_str[0])
    systolic = float(bp_str[1])
    if req['bp_systolic_l'] < systolic > req['bp_systolic_h']:
        return False
    if req['bp_diastolic_l'] < diastolic > req['bp_diastolic_h']:
        return False
    return True


def _facilityqueue_test_bools(user_test, req):
    pos_count = 0
    for k, v in user_test.items():
        if isinstance(v, bool) and v:
            pos_count += 1
            if req[k]:
                return False
    return (pos_count == 0) or pos_count < req['number_of_positives']
