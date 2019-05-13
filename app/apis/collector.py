from flask import request, jsonify
from flask_restplus import Namespace, Resource, fields

from app.CollectorService import CollectorService
from app.models import SensorData
from app.database import db_session


api = Namespace('collector',
                description='Collect data from RPI hotspot'
                )


@api.route('/')
class CollectorResource(Resource):
    def get(self):
        try:
            return CollectorService().get_latest_sensor_data()
        except Exception:
            return dict(message="error in attempt to get latest data"), 500

    def post(self):
        try:
            CollectorService().set_is_collected_to_true()
            return dict(message='success')
        except Exception:
            return dict(message="error in atempt to update is collected to True"), 500
