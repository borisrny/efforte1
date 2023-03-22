from flask import request, g
from flask_login import current_user, login_required

from src.model.hippa import hippa_get_related, hippa_accept
from . import Resource
from .. import schemas


class UsersSelfRelatedUseridHippa(Resource):


    @login_required
    def get(self, userid):
        return hippa_get_related(userid, current_user.id), 200, None


    @login_required
    def post(self, userid):
        return hippa_accept(userid, current_user.id, 'ssn', 'email'), 200, None
