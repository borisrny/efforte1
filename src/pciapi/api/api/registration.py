from flask import request, g

from src.model.registration import registration_post
from . import Resource
from ... import auth_login_plain


class Registration(Resource):

    def post(self):
        rec = g.json
        registration_post(rec)
        _, ret = auth_login_plain(rec['username'], rec['password'])
        return ret, 200, None
