from src.model import user_get_by_phone, user_create, user_update
from src.util import pg_create, util_get_config


def registration_post(rec):
    cnf = util_get_config()
    phone_num = rec.get('phone_number', '')
    if len(phone_num) > 0:
        doc = user_get_by_phone(phone_num)
        if doc is not None:
            roles = doc['roles']
            if roles is None or len(roles) == 0:
                return user_update(doc['id'], {'roles': [cnf['roles']['user']]})
            elif cnf['roles']['user'] not in roles:
                roles.append(cnf['roles']['user'])
                return user_update(doc['id'], {'roles': roles})
            return doc
    if 'roles' not in rec:
        rec['roles'] = [cnf['roles']['user']]
    try:
        return user_create(rec)
    except:
        raise AssertionError('User Name {} already exists'.format(rec['username']))
