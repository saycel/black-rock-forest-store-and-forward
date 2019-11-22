import json

from flask import jsonify

from backend import config
from backend.repositories import SensorRepository


class SensorDataService:
    def get_sensor_data(self, page_size=100, page=1, order="desc"):
        total_count, tuples = SensorRepository().get_sensor_data(
            page_size=page_size, page=page, order=order
        )
        result = [tuple.serialize for tuple in tuples]
        result = [
            dict(
                page=page, total_pages=total_count // page_size, total_count=total_count
            )
        ] + result
        return jsonify(result)

    def insert_many_from_http(
        self, app_key, net_key, device_id, channels, unit_string="U"
    ):
        from backend.app import mqtt_broker
        mqtt_broker.publish(
            config.MQTT_TOPIC,
            json.dumps(
                dict(
                    app_key=app_key,
                    net_key=net_key,
                    device_id=device_id,
                    channels=channels,
                    unit=unit_string,
                )
            ),
        )
