from flask import request, g
from flask_login import current_user, login_required

from src.model import testresult_get_byuser, fmt_date, s3_get_covidtest_url
from . import Resource
from .. import schemas


class UsersSelfCovidtestHistory(Resource):

    @login_required
    def get(self):
        res = testresult_get_byuser('covidtest', current_user.id)
        for doc in res:
            doc['date_of_test'] = fmt_date(doc['date_of_test'])
            doc['pictureURL'] = s3_get_covidtest_url(doc['id'])
        return res, 200, None
