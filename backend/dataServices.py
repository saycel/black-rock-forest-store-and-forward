from flask import jsonify, g

from backend.models import SensorData
from backend.repositories import SensorRepository


class SensorDataService:
    def get_sensor_data(self, page_size=100, page=1):
        total_count, tuples = SensorRepository().get_sensor_data(
            g.current_user.id, page_size, page
        )
        result = [tuple.serialize for tuple in tuples]
        result = [
            dict(
                page=page, total_pages=total_count // page_size, total_count=total_count
            )
        ] + result
        return jsonify(result)

    def insert_many_from_http(self, app_key, net_key, device_id, channels):
        records = []
        for field_name, value in channels.items():
            records.append(
                SensorData(
                    app_key, net_key, device_id, field_name, value, g.current_user.id
                )
            )

        SensorRepository().insert_many(records)
