from flask import request, g
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from src.model import user_get, user_update
from src.util import AppLogicalError, s3_upload_avatar
from . import Resource
from .. import schemas


class UsersSelf(Resource):
    @login_required
    def get(self):
        return user_get(current_user.id), 200, None

    @login_required
    def put(self):
        doc = {k: v for k, v in request.form.items() if k != 'profileImage'}
        user_update(current_user.id, doc)
        if 'profileImage' in request.files:
            file = request.files["profileImage"]
            if file.filename == "":
                raise AppLogicalError(-1, 'Invalid file name.')
            file.filename = secure_filename(file.filename)
            s3_upload_avatar(file, current_user.id)
        return user_get(current_user.id), 200, None
