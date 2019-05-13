from flask import jsonify

from app.repositories import SensorRepository


class CollectorService():
    def get_latest_sensor_data(self):
        tuples = SensorRepository().get_latest_sensor_data()
        result = [tuple.serialize for tuple in tuples]
        return jsonify(result)

    def get_all_sensor_data(self):
        tuples = SensorRepository().get_all_sensor_data()
        result = [tuple.serialize for tuple in tuples]
        return jsonify(result)

    def set_is_collected_to_true(self):
        SensorRepository().set_collected_to_true()
