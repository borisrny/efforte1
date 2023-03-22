from flask import request, g, send_file
from flask_login import login_required, current_user

from src.model import qrcode_user_access_generate
from . import Resource
from .. import schemas


class UsersSelfLaodtestqr(Resource):

    @login_required
    def post(self):
        img = qrcode_user_access_generate(current_user.id, current_user.id)
        return send_file(img, mimetype='image/jpeg')
