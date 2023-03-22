
from flask import request, g
from flask_login import login_required

from src.model import notification_get, notification_update, notification_delete
from . import Resource
from .. import schemas


class BusinessNotificationsNotifid(Resource):


    @login_required
    def get(self, notifid):
        return notification_get(notifid), 200, None


    @login_required
    def put(self, notifid):
        doc = g.json
        doc.pop('postername', None)
        return notification_update(notifid, g.json), 200, None

    @login_required
    def delete(self, notifid):
        return notification_delete(notifid), 200, None