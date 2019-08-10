from flask import request, jsonify
from flask_restplus import Namespace, Resource, fields

from app.CollectorService import CollectorService
from app.models import SensorData
from app.database import db_session


api = Namespace('sensor',
                description='Expose sensor Data'
                )


@api.route('/all')
class SensorResource(Resource):
    def get(self):
        return CollectorService().get_all_sensor_data()


@api.route('/collector/<app_key>/<net_key>/<device_id>/')
class CollectorResource(Resource):
    def get(self, app_key, net_key, device_id):
        try:
            channels = request.args.to_dict()

            for k,v in channels.items():
                try:
                    channels[k] = float(v)
                except Exception as e:
                    return dict(message=f"{k}:{v}, value is not a float or integer"), 400

            record = SensorData(app_key=app_key,
                                net_key=net_key,
                                device_id=device_id,
                                channels=channels)
            db_session.add(record)
            db_session.commit()
        except Exception:
            return dict(message='something went wrong'), 500

        return dict(message='success')
