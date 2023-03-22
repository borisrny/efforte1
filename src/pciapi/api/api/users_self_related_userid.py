from flask import request, g
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from src.model.userrelated import userrelated_get, userrelated_create, userrelated_delete, userrelated_update
from src.util import s3_upload_avatar
from . import Resource
from .. import schemas


class UsersSelfRelatedUserid(Resource):

    @login_required
    def get(self, userid):
        return userrelated_get(current_user.id, userid), 200, None

    def put(self, userid):
        doc = {k: v for k, v in request.form.items() if k != 'profileImage'}
        res = userrelated_update(current_user.id, userid, doc)
        if 'profileImage' in request.files:
            file = request.files["profileImage"]
            if file.filename != "":
                file.filename = secure_filename(file.filename)
                s3_upload_avatar(file, res['id'])
        return userrelated_get(current_user.id, res['id']), 200, None

    def delete(self, userid):
        return userrelated_delete(current_user.id, userid), 200, None
