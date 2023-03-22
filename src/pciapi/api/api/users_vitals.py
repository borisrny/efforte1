from flask import request, g
from flask_login import login_required

from . import Resource
from .. import schemas


class UsersVitals(Resource):

    @login_required
    def get(self):

        return [], 200, None

    @login_required
    def post(self):
        print(g.json)

        return {}, 201, None