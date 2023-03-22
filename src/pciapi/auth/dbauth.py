from singleton_decorator import singleton
from authlib.jose import JWT
from datetime import datetime, timedelta

from src.util import pg_return_connection, pg_get_connection, util_get_config


@singleton
class DBAppAuth:
    def __init__(self):
        self._jwt = JWT()
        with open(util_get_config()['auth']['pubkFile'], 'r') as fh:
            self._pubkey = fh.read()
        with open(util_get_config()['auth']['privkFile'], 'r') as fh:
            self._privkey = fh.read()

    def basic(self, user_id: int, pwd):
        u_id = self.db_auth_check_password(user_id, pwd)
        if u_id > 0:
            token = self.biuld_token(u_id)
            return u_id, token
        raise AssertionError('Invalid user name or password')

    def uid_from_token(self, token):
        claims = self._jwt.decode(token, self._pubkey)
        return claims['userId']

    def db_auth_check_password(self, user_id, pwd):
        sql = 'SELECT id FROM users WHERE username=%s AND password=%s'
        con = pg_get_connection(util_get_config()['pg'])
        cur = con.cursor()
        cur.execute(sql, (user_id, pwd))
        record = cur.fetchone()
        cur.close()
        pg_return_connection(con)
        if record is None:
            raise AssertionError('Invalid user name or password')
        return record[0]

    def biuld_token(self, user_id: int):
        exp_time = datetime.utcnow() + timedelta(weeks=52)
        header = {'alg': 'RS256'}
        payload = {'iss': 'PCI', 'sub': 'PCI', 'exp': exp_time, 'userId': user_id}
        return self._jwt.encode(header, payload, self._privkey)
