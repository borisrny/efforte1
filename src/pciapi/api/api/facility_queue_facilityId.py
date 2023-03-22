from flask import request, g
from flask_login import login_required, current_user

from src.model.facility_queue import facilityqueue_add
from . import Resource
from .. import schemas


class FacilityQueueFacilityid(Resource):

    @login_required
    def post(self, facilityId: int):
        related = g.json
        res = facilityqueue_add(facilityId, current_user.id, related)
        return res, 200, None