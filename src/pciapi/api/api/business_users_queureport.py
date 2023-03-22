from flask import request, g
from flask_login import login_required, current_user
from src.model import business_facilityqueue_report
from src.util import api_str2date
from . import Resource
from .. import schemas


class BusinessUsersQueureport(Resource):

    @login_required
    def get(self):
        stat = int(request.args.get('status', 0))
        role = int(request.args.get('role', 0))
        range_type = int(request.args.get('rangeType', 0))
        from_date = api_str2date(request.args.get('from', 0))
        to_date = api_str2date(request.args.get('to', 0))
        return business_facilityqueue_report(current_user.facilieties[0], stat, role,
                                             range_type, from_date, to_date), 200, None
