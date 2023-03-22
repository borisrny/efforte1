from flask import request, g
from flask_login import current_user, login_required

from src.model.userrelated import userrelated_testresult_get, userrelated_testresult_create
from . import Resource
from .. import schemas


class UsersSelfRelatedUseridQuestionnaire(Resource):

    @login_required
    def get(self, userid):
        return userrelated_testresult_get(current_user.id, 'questionnaire', userid), 200, None

    @login_required
    def post(self, userid):
        return userrelated_testresult_create(current_user.id, 'questionnaire', userid, current_user.id, g.json), 200, None
