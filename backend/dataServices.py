from flask import jsonify, g

from backend.models import SensorData
from backend.repositories import SensorRepository


class SensorDataService:
    def get_sensor_data(self, page_size=100, page=1, order="desc"):
        total_count, tuples = SensorRepository().get_sensor_data(page_size=page_size, page=page, order=order
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
                    app_key=app_key, net_key=net_key, device_id=device_id, field_name=field_name, value=value
                )
            )

        SensorRepository().insert_many(records)
