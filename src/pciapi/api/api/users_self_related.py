from flask import request, g
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename

from src.model.userrelated import userrelated_list, userrelated_create, userrelated_get
from src.util import s3_upload_avatar
from . import Resource
from .. import schemas


class UsersSelfRelated(Resource):

    @login_required
    def get(self):
        return userrelated_list(current_user.id), 200, None

    @login_required
    def post(self):
        doc = {k: v for k, v in request.form.items() if k != 'profileImage'}
        res = userrelated_create(current_user.id, doc)
        if 'profileImage' in request.files:
            file = request.files["profileImage"]
            if file.filename != "":
                file.filename = secure_filename(file.filename)
                s3_upload_avatar(file, res['id'])
        return userrelated_get(current_user.id, res['id']), 200, None