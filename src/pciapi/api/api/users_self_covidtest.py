from flask import request, g
from werkzeug.utils import secure_filename

from src.util import s3_upload_covidtest, s3_upload_requisition, fmt_date, to_bool
from . import Resource
from .. import schemas
from flask_login import login_required, current_user
from src.model import testresult_last_byuser, testresult_create


class UsersSelfCovidtest(Resource):

    @login_required
    def get(self):
        doc = testresult_last_byuser('covidtest', current_user.id)
        if doc is not None:
            doc['date_of_test'] = fmt_date(doc['date_of_test']) if doc else {}
        return doc, 200, None

    @login_required
    def post(self):
        doc = {k: to_bool(v) for k, v in request.form.items() if k != 'date_of_test'}
        doc['date_of_test'] = request.form.get('date_of_test')
        resp = testresult_create('covidtest', current_user.id, current_user.id, doc)

        picture = request.files.get("picture")
        if picture is not None and picture.filename != "":
            picture.filename = secure_filename(picture.filename)
            s3_upload_covidtest(picture, resp['id'])

        requisition = request.files.get("requisition")
        if requisition is not None and requisition.filename != "":
            requisition.filename = secure_filename(requisition.filename)
            s3_upload_requisition(requisition, resp['id'])

        return resp, 200, None
