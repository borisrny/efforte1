from flask import request, g
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename

from src.util import AppLogicalError, s3_upload_avatar
from . import Resource
from .. import schemas


class UsersSelfImage(Resource):

    @login_required
    def post(self):
        if 'avatar' not in request.files:
            raise AppLogicalError(-1, 'No file in request.')
        file = request.files["avatar"]
        if file.filename == "":
            raise AppLogicalError(-1, 'Invalid file name.')
        file.filename = secure_filename(file.filename)
        s3_upload_avatar(file, current_user.id)
