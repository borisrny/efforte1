from flask import request, g
from flask_login import login_required, current_user

from src.model import testresult_get_byuser, testresult_create
from . import Resource
from .. import schemas


class TestfacilityPatientsUseridCovid(Resource):

    @login_required
    def get(self, userId):
        return testresult_get_byuser('covidtest', userId), 200, None

    @login_required
    def post(self, userId):
        res = testresult_create('covidtest', userId, current_user.id, g.json)
        return res, 201, None