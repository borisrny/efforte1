from flask import request, g
from flask_login import login_required

from src.model import business_list, business_create
from . import Resource
from .. import schemas


class ConsoleBusinesses(Resource):

    @login_required
    def get(self):
        tmp = request.args.get('businessType', None)
        return business_list({'businessType': tmp}), 200, None

    @login_required
    def post(self):
        tmp = request.args.get('businessType', None)
        doc = g.json.copy()
        doc['facilitytype'] = tmp
        res = business_create(doc)
        return res, 201, None
