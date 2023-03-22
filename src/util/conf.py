import yaml

app_cnf = {}


def merge_dict(source, destination):
    for key, value in list(source.items()):
        if isinstance(value, dict):
            # get node or create one
            node = destination.setdefault(key, {})
            merge_dict(value, node)
        else:
            destination[key] = value

    return destination


def util_init_config(fn):
    cnf = {}
    with open(fn, 'r') as ymlfile:
        cnf = yaml.load(ymlfile, Loader=yaml.FullLoader)
    for inc in cnf.get('include', []):
        cnf = merge_dict(cnf, yaml.load(open(inc), Loader=yaml.FullLoader))
    global app_cnf
    app_cnf = cnf


def util_get_config():
    global app_cnf
    return app_cnf


def util_apptype_to_role(app_type):
    role_acro = app_cnf['appTypeRoleMap'][app_type]
    return app_cnf['roles'][role_acro]


def util_user_accept_status_to_str(stat: int):
    cnf_stat = util_get_config()['userStatusMap']
    for k, v in cnf_stat.items():
        if v == stat:
            return k
    return ''
