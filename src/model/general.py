from src.util import util_get_config


def general_terms():
    cnf = util_get_config()
    with open(cnf['terms']['file'], 'r') as fl:
        txt = fl.read()
    return txt


def general_about():
    cnf = util_get_config()
    return {'name': cnf['about']['name'], 'contact': cnf['about']['contact']}
