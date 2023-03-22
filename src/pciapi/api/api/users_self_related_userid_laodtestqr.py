from flask import request, g, send_file
from flask_login import current_user, login_required

from src.model import qrcode_user_access_generate
from . import Resource
from .. import schemas


class UsersSelfRelatedUseridLaodtestqr(Resource):

    @login_required
    def post(self, userid):
        img = qrcode_user_access_generate(current_user.id, userid)
        return send_file(img, mimetype='image/jpeg')
