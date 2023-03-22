from flask import request, g
from flask_login import login_required
from . import Resource

from src.model import user_get, user_create, user_delete, user_update


class UsersUserid(Resource):

    @login_required
    def get(self, userid):
        return user_get(userid), 200, None

    @login_required
    def put(self, userid):
        return user_update(userid, g.json), 200, None

    @login_required
    def delete(self, userid):
        return user_delete(userid), 200, None
