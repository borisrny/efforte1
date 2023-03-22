from flask import request, g
from flask_login import login_required
from . import Resource
from .. import schemas

from src.model import user_list, memberuser_add


class ConsoleBusinessesBusinessidMembers(Resource):

    @login_required
    def get(self, businessid):
        return user_list({'businessId': businessid}), 200, None

    @login_required
    def post(self, businessid):
        return memberuser_add(businessid, g.json), 200, None