from __future__ import absolute_import, print_function
from flask import request, g
from flask_login import login_required, current_user

from src.model.userinvite import userinvite_invite
from . import Resource
from .. import schemas


class BusinessUsersUseridInvite(Resource):

    @login_required
    def post(self, userid):
        return userinvite_invite(userid, current_user.id, current_user.facilieties[0]), 200, None
