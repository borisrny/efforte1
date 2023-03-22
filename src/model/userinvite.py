import logging

from psycopg2 import extras

from src.model import user_get, business_get
from src.util import pg_get_connection, pg_return_connection, util_get_config, send_sms, pg_get, pg_update
from src.util.conf import util_user_accept_status_to_str


def userinvite_invite(user_id, invite_user_id, bussiness_id):
    cnf = util_get_config()
    sql = """
    INSERT INTO userfacilitytestaccess (userid, facilityid, postuser, updateuser, status)\
    VALUES ({user_id}, {bussiness_id}, {invite_user_id}, {invite_user_id}, {status})\
    ON CONFLICT (userid, facilityid) DO\
    UPDATE SET status = {status}, postuser={invite_user_id} RETURNING id
    """.format(user_id=user_id, invite_user_id=invite_user_id,
               bussiness_id=bussiness_id, status=cnf['userStatusMap']['Pending'])
    con = pg_get_connection(cnf['pg'])
    cur = con.cursor()
    cur.execute(sql)
    recid = cur.fetchone()[0]
    con.commit()
    pg_return_connection(con)
    code = '{}-{}-{}'.format(recid, user_id, bussiness_id)
    user = user_get(user_id)
    business = business_get(bussiness_id)
    phone_number = user.get('phone_number')
    b_name = business.get('name')
    text = 'Dear {fn} {ln}. Please accept invitation from {bn} to join PCS. Access code: {code}'. \
        format(fn=user.get('first_name'), ln=user.get('last_name'), bn=b_name, code=code)
    send_sms(phone_number, text)


def userinvite_suspend(user_id, invite_user_id, bussiness_id):
    cnf = util_get_config()
    sql = """
    UPDATE userfacilitytestaccess SET status = {status}, postuser={invite_user_id}\
    WHERE userid={user_id} AND facilityid={bussiness_id}
    """.format(user_id=user_id, invite_user_id=invite_user_id,
               bussiness_id=bussiness_id, status=cnf['userStatusMap']['Suspended'])
    con = pg_get_connection(cnf['pg'])
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    pg_return_connection(con)


def userinvite_accept(user_id, invite_code):
    toks = invite_code.split('-')
    if len(toks) != 3:
        raise AssertionError('Invalid token {}'.format(invite_code))
    iid = int(toks[0].replace(' ', ''))
    userid = int(toks[1].replace(' ', ''))
    bid = int(toks[2].replace(' ', ''))
    if userid != user_id:
        raise AssertionError('Token from unexpected user {}')
    cnf = util_get_config()
    invite = pg_get(cnf, 'userfacilitytestaccess', iid)
    if invite is None:
        raise AssertionError('Invalid token (no invitation)')

    if invite['facilityid'] != bid or invite['userid'] != user_id:
        raise AssertionError('Invalid token (attributes do not match).')
    if invite['status'] != cnf['userStatusMap']['Pending']:
        raise AssertionError('Unexpected invitation status: {}'.format(invite['status']))
    pg_update(cnf, 'userfacilitytestaccess', iid, {'status': cnf['userStatusMap']['Active']})


def userinvite_user_list(user_id):
    sql = 'SELECT rec.*, fac.name FROM userfacilitytestaccess rec, facility fac ' \
          'WHERE rec.userid=%s AND fac.id=rec.facilityid'
    con = pg_get_connection(util_get_config()['pg'])
    cur = con.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute(sql, (user_id,))
    data = []
    for i in cur.fetchall():
        data.append({
            'id': i['id'],
            'status': util_user_accept_status_to_str(i['status']),
            'name': i['name']
        })
    cur.close()
    pg_return_connection(con)
    return data

def userinvite_remove(user_id, recid):
    cnf = util_get_config()
    pg_update(cnf, 'userfacilitytestaccess', recid, {'status': cnf['userStatusMap']['Deleted']})
    return userinvite_user_list(user_id)
