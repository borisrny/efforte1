from flask import request, g
from flask_login import login_required, current_user

from src.model import user_list, user_create
from . import Resource
from .. import schemas
from ... import auth_perm_filter


class Users(Resource):

    @login_required
    def get(self):
        fltr = {}
        component = request.args.get('component', None)
        role = request.args.get('role', 0)
        status = request.args.get('status', 0)
        if component is not None:
            fltr['component'] = component
        fltr.update(auth_perm_filter())
        if role != 0:
            fltr['role'] = int(role)
        if status != 0:
            fltr['status'] = int(status)
        ret = user_list(fltr)
        return ret, 200, None

    @login_required
    def post(self):
        print(g.json)

        return {}, 201, None