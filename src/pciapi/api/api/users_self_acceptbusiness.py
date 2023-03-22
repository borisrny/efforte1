from flask import request, g
from flask_login import current_user, login_required

from src.model.userinvite import userinvite_accept, userinvite_user_list
from . import Resource
from .. import schemas


class UsersSelfAcceptbusiness(Resource):

    @login_required
    def get(self):
        return userinvite_user_list(current_user.id), 200, None

    @login_required
    def put(self):
        userinvite_accept(current_user.id, g.json.get('token'))
        return None, 200, None
