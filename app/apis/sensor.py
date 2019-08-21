from flask import request
from flask_restplus import Namespace, Resource

from app.dataServices import SensorDataService


api = Namespace('sensor',
                description='Expose sensor Data'
                )


@api.route('/all')
class SensorResource(Resource):
    def get(self):
        return SensorDataService().get_all_sensor_data()


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
                SensorDataService().insert_many_from_http(app_key, net_key, device_id, channels)
        except Exception as e:
            return dict(message=f'something went wrong trying to insert values with http  error:{e.args[0]}'), 500

        return dict(message='success')
