# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class BusinessUsersUserid(Resource):

    def get(self, userid):

        return {}, 200, None

    def delete(self, userid):

        return {}, 200, None