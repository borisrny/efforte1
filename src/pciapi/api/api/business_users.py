from flask import request, g
from flask_login import login_required

from src.model import user_list
from . import Resource
from .. import schemas
from ... import auth_perm_filter


class BusinessUsers(Resource):

    @login_required
    def get(self):
        fltr = auth_perm_filter()
        return user_list(fltr), 201, None

    @login_required
    def post(self):
        print(g.json)

        return {}, 201, None
