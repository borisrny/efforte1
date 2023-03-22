from flask import request, g
from flask_login import login_required, current_user

from src.model import bussiness_testrequirements_get, bussiness_testrequirements_upsert
from . import Resource
from .. import schemas


class BusinessTestrequirements(Resource):

    @login_required
    def get(self):
        return bussiness_testrequirements_get(current_user.facilieties[0]), 200, None

    @login_required
    def post(self):
        return bussiness_testrequirements_upsert(current_user.facilieties[0], g.json), 200, None

    @login_required
    def put(self):
        return bussiness_testrequirements_upsert(current_user.facilieties[0], g.json), 200, None
