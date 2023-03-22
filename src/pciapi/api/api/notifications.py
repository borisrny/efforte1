from flask import request, g
from flask_login import login_required, current_user

from src.model import notification_list, notification_create
from . import Resource
from .. import schemas


class Notifications(Resource):

    def get(self):
        return notification_list(), 200, None


    @login_required
    def post(self):
        return notification_create(current_user.id, None, g.json), 201, None
