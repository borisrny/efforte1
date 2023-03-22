from flask import request, g
from flask_login import login_required

from src.model import business_list, business_create
from . import Resource
from .. import schemas


class Facilities(Resource):

    @login_required
    def get(self):
        return business_list({'businessType': 'facility'}), 200, None

    @login_required
    def post(self):
        doc = g.json
        if 'facilitytype' not in doc:
            doc['facilitytype'] = 'facility'
        return business_create(doc), 200, None