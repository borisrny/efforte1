from flask import request, g
from flask_login import login_required, current_user

from src.model import business_health_report
from . import Resource
from .. import schemas


class BusinessUsersHealth(Resource):

    @login_required
    def get(self):
        stat = int(request.args.get('status', 0))
        role = int(request.args.get('role', 0))
        return business_health_report(current_user.facilieties[0], stat, role), 200, None
