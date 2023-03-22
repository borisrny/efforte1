import random
import string
from base64 import b64decode
import logging

from flask_login import LoginManager
from flask_login import UserMixin
from flask_login import current_user

from src.model import memberuser_get_user, user_get, util_get_config, pg_update
from src.pciapi.auth.dbauth import DBAppAuth
from src.util import util_apptype_to_role, send_sms


class AuthUser(UserMixin):
    def __init__(self, userid, roles, facilieties):
        self.id = userid
        self.roles = roles
        self.facilieties = facilieties


def auth_setup(app):
    login_manager = LoginManager(app)

    @login_manager.request_loader
    def load_user_from_rqst(rqst):
        user = auth_uid_from_rqst(rqst)
        return user

    @login_manager.user_loader
    def load_user(user_id):
        raise Exception('login_manager.user_loader')


def auth_login(rqst):
    auth_headers = rqst.headers.get('Authorization')
    auth_keys = auth_headers.split()
    if auth_keys[0] == 'Basic':
        header_val = b64decode(auth_keys[1]).decode('utf-8')
        user_id, pwd = header_val.split(':')
        u_id, ret = auth_login_plain(user_id, pwd)
        app_type = rqst.args.get('appType', None)
        if app_type is not None:
            user = user_get(u_id)
            required_role = util_apptype_to_role(app_type)
            if required_role not in user['roles']:
                raise AssertionError('Insufficient privileges')
        return ret
    raise AssertionError('Expected Basic authentication')


def auth_login_plain(user_id, pwd):
    u_id, token = DBAppAuth().basic(user_id, pwd)
    return u_id, {'token': token.decode("utf-8")}


def auth_uid_from_rqst(rqst):
    auth_headers = rqst.headers.get('Authorization')
    auth_keys = auth_headers.split()
    if auth_keys[0] == 'Bearer':
        token = auth_keys[1].encode("utf-8")
        u_id = DBAppAuth().uid_from_token(token)
        rec = memberuser_get_user(u_id)
        return AuthUser(u_id, rec['roles'], rec['facilieties'])


def auth_perm_filter():
    cnf = util_get_config()
    if cnf['roles']['admin'] in current_user.roles:
        return {}
    if cnf['roles']['HR'] in current_user.roles:
        return {'allow_facilieties': current_user.facilieties}
    return {'allow_facilieties': [0]}


def auth_change_password(user_id, old_pwd, new_pwd):
    pg_update(util_get_config(), 'users', user_id, {'password': new_pwd})


def auth_forgot_password(phone_number):
    new_pwd = auth_generate_password()
    pg_update(util_get_config(), 'users', "'{}'".format(phone_number), {'password': new_pwd}, 'phone_number')
    send_sms(phone_number, 'Your new password is: {}. Please change'.format(new_pwd))


def auth_generate_password():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(8))
