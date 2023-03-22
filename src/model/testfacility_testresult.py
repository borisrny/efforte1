from src.model import testresult_create
from src.util import pg_get, util_get_config


def testfacility_testresult_vitals_add(facilityId, user_key, doc):
    cnf = util_get_config()
    rec = pg_get(cnf, 'tempuserwaccess', recid=user_key, idfield='akey')
    if rec:
        user_id = rec['userid']
        # doc['postfacility'] = rec['facilityId']
        testresult_create('vitals', user_id, 0, doc)