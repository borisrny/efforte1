import logging

from src.model import user_create, pg_create, user_get, business_get
from src.model.registration import registration_post
from src.util import pg_get_connection, util_get_config, pg_return_connection


def memberuser_add(business_id, user_doc):
    doc = user_create(user_doc)
    pg_create(util_get_config(), 'userfacility',
              {'userid': doc['id'], 'facilityid': business_id},
              'facilityid')
    return doc


def memberuser_get_user(recid):
    user_rec = user_get(recid)
    sql = 'select facilityid from userfacility where userid={}'.format(recid)
    con = pg_get_connection(util_get_config()['pg'])
    cur = con.cursor()
    cur.execute(sql)
    user_rec['facilieties'] = [i[0] for i in cur.fetchall()]
    cur.close()
    pg_return_connection(con)
    return user_rec


def memberuser_get_user_description(userid, f_id):
    user_rec = user_get(userid)
    fac_rec = business_get(f_id)
    return {
        'username': user_rec['username'],
        'firstName': user_rec['first_name'],
        'lastName': user_rec['last_name'],
        'companyName': fac_rec['name']
    }


def memberuser_register(business_id, user_doc):
    cnf = util_get_config()
    user_rec = registration_post(user_doc)

    try:
        pg_create(cnf, 'userfacility',
                  {'userid': user_rec['id'], 'facilityid': business_id},
                  'facilityid')
    except Exception as ex:
        logging.getLogger(__name__).info(ex)
    return user_get(user_rec['id'])
