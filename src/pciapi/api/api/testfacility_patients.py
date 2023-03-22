from flask import request, g
from flask_login import login_required

from src.model import user_like
from . import Resource
from .. import schemas


class TestfacilityPatients(Resource):

    @login_required
    def get(self):
        fltr = {k: v for k, v in request.args.items()}
        if len(fltr) < 1:
            raise AssertionError('Filter has to be n ot empty')
        return user_like(fltr), 200, None