
from flask import request, g

from . import Resource
from .. import schemas
from ...auth.auth import auth_forgot_password


class Forgotpassword(Resource):


    def post(self):
        auth_forgot_password(g.json.get('email'))
        return None, 200, None
