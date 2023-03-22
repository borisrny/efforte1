from flask import request, g
from flask_login import login_required, current_user

from src.model.userrelated import userrelated_testresult_list
from src.util import fmt_date, s3_get_covidtest_url
from . import Resource
from .. import schemas


class UsersSelfRelatedUseridCovidtestHistory(Resource):

    @login_required
    def get(self, userid):
        res = userrelated_testresult_list(current_user.id, 'covidtest', userid)
        for doc in res:
            doc['date_of_test'] = fmt_date(doc['date_of_test'])
            doc['pictureURL'] = s3_get_covidtest_url(doc['id'])
        return res, 200, None
