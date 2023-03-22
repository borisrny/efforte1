# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from src.model import general_terms
from . import Resource
from .. import schemas


class Terms(Resource):

    def get(self):
        return general_terms(), 200, None