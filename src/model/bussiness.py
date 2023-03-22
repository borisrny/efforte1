from .facility_base import *
from src.util import util_get_config, pg_get, pg_delete, pg_update, pg_create


def business_list(fltr):
    cnf = util_get_config()
    type_id = cnf['businessType'][fltr.get('businessType')]
    return facility_base_list(cnf, type_id, fltr)


def business_get(recid):
    return pg_get(util_get_config(), 'facility', recid)


def business_create(doc):
    doc.pop('id', None)
    facilitytype = doc['facilitytype']
    cnf = util_get_config()
    if not isinstance(facilitytype, int):
        doc['facilitytype'] = cnf['businessType'][facilitytype]
    rec_id = pg_create(cnf, 'facility', doc)
    return business_get(rec_id)


def business_delete(recid):
    return pg_delete(util_get_config(), 'facility', recid)


def business_update(recid, doc):
    doc.pop('id', None)
    return pg_update(util_get_config(), 'facility', recid, doc)


