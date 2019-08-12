from flask import jsonify

from app.database import db_session
from app.models import SensorData
from app.repositories import SensorRepository


class SensorDataService():

    def get_all_sensor_data(self):
        tuples = SensorRepository().get_all_sensor_data()
        result = [tuple.serialize for tuple in tuples]
        return jsonify(result)

    def insert_many_from_http(self, app_key, net_key, device_id, channels):
        records = []
        for field_name, value in channels.items():
            records.append(SensorData(app_key,
                                      net_key,
                                      device_id,
                                      field_name,
                                      value
                                      ))

        SensorRepository.insert_many(records)

