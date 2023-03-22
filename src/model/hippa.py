from src.model import user_get
from src.model.userrelated import userrelated_get
from src.util import util_get_config


def hippa_get(userid):
    cnf = util_get_config()
    res = ''
    related = parent = user_get(userid)
    with open(cnf['hippa']['file'], 'r') as fl:
        txt = fl.read()
        res = txt.format(owner_name=_hippa_get_name(parent), owner_dob=parent['dob'],
                         dep_name='', dep_reason='')
    return {'text': res, 'ssn': parent['ssn']}


def hippa_get_related(userid, parentid):
    cnf = util_get_config()
    res = ''
    parent = user_get(parentid)
    related = userrelated_get(parentid, userid)
    with open(cnf['hippa']['file'], 'r') as fl:
        txt = fl.read()
        res = txt.format(owner_name=_hippa_get_name(parent), owner_dob=parent['dob'],
                         dep_name=_hippa_get_name(related), dep_reason=related['relationreason'])
    return {'text': res, 'ssn': related['ssn']}


def hippa_accept(userid, parentid, ssn, rend_email):
    pass


def _hippa_get_name(rec):
    fn = rec.get('first_name')
    if fn == None:
        fn = ''
    ln = rec.get('last_name')
    if ln == None:
        ln = ''
    return ' '.join((fn, ln))
