from flask import request, g
from flask_login import login_required, current_user

from src.model import memberuser_get_user_description
from . import Resource
from .. import schemas


class UsersSelfLogindescription(Resource):

    @login_required
    def get(self):
        ret = memberuser_get_user_description(current_user.id, current_user.facilieties[0])
        return ret, 200, None