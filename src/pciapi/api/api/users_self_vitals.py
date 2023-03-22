import logging

from flask import request, g
from flask_login import login_required, current_user

from src.model import testresult_create, testresult_get_byuser
from src.util import fmt_date_tm
from . import Resource
from .. import schemas


class UsersSelfVitals(Resource):

    @login_required
    def get(self):
        # postdate
        res = testresult_get_byuser('vitals', current_user.id)
        for r in res:
            r['postdate'] = fmt_date_tm(r['posttimestamp'])
            logging.getLogger(__name__).info(fmt_date_tm(r['posttimestamp']))

        return res, 200, None

    @login_required
    def post(self):
        return testresult_create('vitals', current_user.id, current_user.id, g.json), 200, None
