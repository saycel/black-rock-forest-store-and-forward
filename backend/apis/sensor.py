from flask import request
from flask_restplus import Namespace, Resource
from backend.dataServices import SensorDataService
from backend.token_auth import auth_needed

api = Namespace("sensor", description="Expose sensor Data")


@api.route("/data/<int:page_size>/<int:page>")
class SensorResource(Resource):
    @auth_needed
    def get(self, page_size, page):
        if page_size < 0 or page < 0:
            return dict(message="page_size and page must be positive integers"), 400
        if page_size > 500:
            return dict(message="page_size limit 500")
        return SensorDataService().get_sensor_data(page_size, page)


@api.route("/collector/<app_key>/<net_key>/<device_id>/")
class CollectorResource(Resource):
    @auth_needed
    def get(self, app_key, net_key, device_id):
        try:
            channels = request.args.to_dict()
            for k, v in channels.items():
                try:
                    channels[k] = float(v)
                except Exception as e:
                    return (
                        dict(message=f"{k}:{v}, value is not a float or integer"),
                        400,
                    )
            SensorDataService().insert_many_from_http(
                app_key, net_key, device_id, channels
            )
        except Exception as e:
            return (
                dict(
                    message=f"something went wrong trying to insert values with http  error:{e.args[0]}"
                ),
                500,
            )

        return dict(message="success")
