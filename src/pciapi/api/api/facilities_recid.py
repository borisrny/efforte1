from flask import request, g
from flask_login import login_required
from . import Resource
from .. import schemas

from src.model import business_update


class FacilitiesRecid(Resource):

    @login_required
    def put(self, recid):
        return business_update(recid, g.json), 200, None