from flask import request, g
from flask_login import login_required, current_user

from src.model.facility_queue import facilityqueue_get
from . import Resource
from .. import schemas


class FacilityQueue(Resource):

    @login_required
    def get(self):
        return facilityqueue_get(current_user.facilieties[0]), 200, None