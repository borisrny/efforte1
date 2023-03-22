from flask import request, g
from flask_login import current_user
from . import Resource
from .. import schemas


class BusinessUsersUseridSuspend(Resource):

    def post(self, userid):
        return userinvite_suspend(userid, current_user.id, current_user.facilieties[0]), 200, None
