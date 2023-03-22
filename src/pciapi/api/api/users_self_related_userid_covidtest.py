import logging

from flask import request, g
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from src.model.userrelated import userrelated_testresult_get, userrelated_testresult_create
from src.util import s3_upload_covidtest, s3_upload_requisition
from src.util.common import to_bool
from . import Resource
from .. import schemas


class UsersSelfRelatedUseridCovidtest(Resource):

    @login_required
    def get(self, userid):
        return userrelated_testresult_get(current_user.id, 'covidtest', userid), 200, None

    @login_required
    def post(self, userid):
        doc = {k: to_bool(v) for k, v in request.form.items() if k != 'date_of_test'}
        doc['date_of_test'] = request.form.get('date_of_test')
        resp = userrelated_testresult_create(current_user.id, 'covidtest', userid, current_user.id, doc)

        picture = request.files.get("picture")
        if picture is not None and picture.filename != "":
            picture.filename = secure_filename(picture.filename)
            s3_upload_covidtest(picture, resp['id'])

        requisition = request.files.get("requisition")
        if requisition is not None and requisition.filename != "":
            requisition.filename = secure_filename(requisition.filename)
            s3_upload_requisition(requisition, resp['id'])

        return resp, 200, None
