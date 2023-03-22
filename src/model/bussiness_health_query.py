from psycopg2 import extras

from src.model import bussiness_testrequirements_get, user_list, user_get_by_ids, s3_get_profile_url, \
    testresult_last_byuser_ids, s3_get_covidtest_url
from src.model.facility_queue import facilityqueue_pass
from src.util import pg_get_connection, util_get_config, pg_return_connection


def business_health_report(f_id, health_stat, role):
    requirements = bussiness_testrequirements_get(f_id)
    users = user_list({'businessId': f_id, 'role': role})
    facility_queue_users = {i['id']: {'user': i} for i in users}
    ids = list(facility_queue_users.keys())
    # for u in user_get_by_ids(ids):
    #     u['avatar'] = s3_get_profile_url(u['id'])
    #     users[u['id']]['user'] = u
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
    if health_stat != 0:
        res = filter(lambda u: u['requirementsMatch'] == (health_stat == 1), res)
    return res


def business_facilityqueue_report(f_id, health_stat, role, range_type, from_date, to_date):
    range_types = ['time_requested', 'time_in']
    requirements = bussiness_testrequirements_get(f_id)
    sql = "SELECT * FROM customerqueu WHERE facilityid=%s " \
          "AND {0} BETWEEN \'{1}\' AND \'{2}\' " \
          "ORDER BY {0} ASC" \
        .format(range_types[range_type], from_date, to_date)
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
