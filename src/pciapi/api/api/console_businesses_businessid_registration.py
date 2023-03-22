from flask import request, g
from flask_login import login_required
from . import Resource
from .. import schemas
from src.model import memberuser_register


class ConsoleBusinessesBusinessidRegistration(Resource):

    @login_required
    def post(self, businessid):
        role = request.args.get('userRole', 'user')
        return memberuser_register(businessid, role, g.json), 200, None