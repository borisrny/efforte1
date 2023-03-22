from flask import request, g
from flask_login import login_required

from src.model import user_get
from . import Resource
from .. import schemas


class TestfacilityPatientsUserid(Resource):

    @login_required
    def get(self, userId):
        return user_get(userId), 200, None