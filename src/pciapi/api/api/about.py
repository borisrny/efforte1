# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from src.model import general_about
from . import Resource
from .. import schemas


class About(Resource):

    def get(self):
        return general_about(), 200, None