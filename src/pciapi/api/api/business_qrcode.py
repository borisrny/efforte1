from flask import request, g
from flask_login import login_required, current_user

from src.model import qrcode_facility_queue_get, qrcode_facility_queue_generate
from . import Resource
from .. import schemas


class BusinessQrcode(Resource):

    @login_required
    def get(self):
        return qrcode_facility_queue_get(current_user.facilieties[0]), 200, None

    @login_required
    def post(self):
        return qrcode_facility_queue_generate(current_user.facilieties[0]), 200, None
