# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
from flask_login import current_user, login_required

from src.model.hippa import hippa_get, hippa_accept
from . import Resource
from .. import schemas


class UsersSelfHippa(Resource):

    @login_required
    def get(self):
        return hippa_get(current_user.id), 200, None

    @login_required
    def post(self):
        return hippa_accept(current_user.id, current_user.id, 'ssn', 'email'), 200, None
