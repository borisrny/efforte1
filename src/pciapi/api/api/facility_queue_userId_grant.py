from flask import request, g
from flask_login import login_required, current_user

from src.model.facility_queue import facilityqueue_grant
from . import Resource
from .. import schemas


class FacilityQueueUseridGrant(Resource):

    @login_required
    def put(self, userId: int):
        grant = request.args.get('status')
        return facilityqueue_grant(current_user.facilieties[0], userId, grant == 'true'), 200, None
