import logging

from flask import request, g
from flask_login import current_user, login_required

from . import Resource
from .. import schemas
from ...auth.auth import auth_change_password


class Changepassword(Resource):

    @login_required
    def post(self):
        auth_change_password(current_user.id, g.json.get('oldPassword'), g.json.get('newPassword'))
        return {'status': 'ok'}, 200, None