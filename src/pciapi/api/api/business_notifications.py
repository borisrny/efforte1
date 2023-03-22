from flask import request, g
from flask_login import current_user, login_required

from src.model import notification_list, notification_create
from . import Resource
from .. import schemas


class BusinessNotifications(Resource):

    @login_required
    def get(self):
        res = notification_list({'facility': current_user.facilieties[0]})
        return res, 200, None

    def post(self):
        return notification_create(current_user.id, current_user.facilieties[0], g.json), 201, None