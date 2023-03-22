from flask import request, g

from . import Resource
from src.pciapi.auth import auth_login


class Auth(Resource):

    def post(self):
        return auth_login(request), 200, None
