from flask import request, g
from flask_login import login_required

from src.model import business_create, business_list
from . import Resource
from .. import schemas


class Testfacilities(Resource):

    @login_required
    def get(self):
        return business_list({'businessType': 'testfacility'}), 200, None

    @login_required
    def post(self):
        doc = g.json
        if 'facilitytype' not in doc:
            doc['facilitytype'] = 'testfacility'
        return business_create(doc), 200, None