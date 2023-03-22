from flask import request, g
from flask_login import login_required, current_user

from src.model import memberuser_register
from . import Resource
from .. import schemas
from ... import auth_perm_filter


class BusinessesRegistration(Resource):

    @login_required
    def post(self):
        perm = auth_perm_filter()
        return memberuser_register(perm['allow_facilieties'][0], g.json), 200, None