from flask import request, g
from flask_login import login_required

from . import Resource
from .. import schemas


class VitalsCurrent(Resource):

    @login_required
    def get(self):
        return {}, 201, None
