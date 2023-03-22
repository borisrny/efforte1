from flask import request, g
from . import Resource
from .. import schemas
from flask_login import login_required, current_user
from src.model import testresult_last_byuser, testresult_create


class UsersSelfQuestionnaire(Resource):

    @login_required
    def get(self):
        return testresult_last_byuser('questionnaire', current_user.id), 200, None

    @login_required
    def post(self):
        return testresult_create('questionnaire', current_user.id, current_user.id, g.json), 200, None
