# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
from flask_login import login_required, current_user

from src.model.userrelated import userrelated_testresult_list, userrelated_testresult_create
from . import Resource
from .. import schemas


class UsersSelfRelatedUseridVitals(Resource):

    @login_required
    def get(self, userid):
        return userrelated_testresult_list(current_user.id, 'vitals', userid), 200, None

    @login_required
    def post(self, userid):
        resp = userrelated_testresult_create(current_user.id, 'vitals', userid, current_user.id, g.json)
        return resp, 200, None
