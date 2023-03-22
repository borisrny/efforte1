from src.util import util_get_config, pg_get, pg_delete, pg_update, pg_create


def bussiness_testrequirements_get(bussiness_id):
    cnf = util_get_config()
    res = {
        'vitalRequirements': pg_get(cnf, 'vitalsfilter', bussiness_id, 'facilityid'),
        'covidTest': pg_get(cnf, 'covidtestfilter', bussiness_id, 'facilityid'),
        'questionnaireRequirements': pg_get(cnf, 'questionnairefilter', bussiness_id, 'facilityid')
    }
    return res


def bussiness_testrequirements_upsert(bussiness_id, doc):
    cnf = util_get_config()
    vit = doc['vitalRequirements']
    vit['facilityid'] = bussiness_id
    cov = doc['covidTest']
    cov['facilityid'] = bussiness_id
    quest = doc['questionnaireRequirements']
    quest['facilityid'] = bussiness_id

    recid = vit.pop('id', 0)
    if recid == 0:
        pg_create(cnf, 'vitalsfilter', vit)
    else:
        pg_update(cnf, 'vitalsfilter', recid, vit)

    recid = cov.pop('id', 0)
    if recid == 0:
        pg_create(cnf, 'covidtestfilter', cov)
    else:
        pg_update(cnf, 'covidtestfilter', recid, cov)

    recid = quest.pop('id', 0)
    if recid == 0:
        pg_create(cnf, 'questionnairefilter', quest)
    else:
        pg_update(cnf, 'questionnairefilter', recid, quest)

    return bussiness_testrequirements_get(bussiness_id)

