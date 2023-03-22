from flask import request, g
from flask_login import login_required, current_user

from src.model.userinvite import userinvite_remove
from . import Resource
from .. import schemas

class UsersSelfAcceptbusinessRecordid(Resource):

    @login_required
    def delete(self, recordId):
        return userinvite_remove(current_user.id, recordId), 200, None