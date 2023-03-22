# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from src.model.testfacility_testresult import testfacility_testresult_vitals_add
from . import Resource
from .. import schemas


class LoadtestVitalsUserkeyFacilityid(Resource):

    def post(self, userKey, facilityId):
        testfacility_testresult_vitals_add(facilityId, userKey, g.json)
        return None, 201, None