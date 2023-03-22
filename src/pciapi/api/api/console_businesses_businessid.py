from flask import request, g
from flask_login import login_required

from src.model import business_get, business_update, business_delete
from . import Resource
from .. import schemas


class ConsoleBusinessesBusinessid(Resource):

    @login_required
    def get(self, businessid):
        return business_get(businessid), 200, None

    @login_required
    def put(self, businessid):
        return business_update(businessid, g.json), 200, None

    @login_required
    def delete(self, businessid):
        business_delete(businessid)
        return None, 200, None