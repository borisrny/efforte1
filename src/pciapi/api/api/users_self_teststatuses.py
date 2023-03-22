from flask import request, g
from flask_login import login_required, current_user

from src.model.userrelated import user_get_testsummaries
from . import Resource
from .. import schemas


class UsersSelfTeststatuses(Resource):

    @login_required
    def get(self):
        return user_get_testsummaries(current_user.id, ), 200, None
