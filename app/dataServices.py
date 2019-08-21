import io
import pandas as pd
from flask import jsonify
from multiprocessing import Pool

from app.database import db_session
from app.models import SensorData
from app.repositories import SensorRepository


class SensorDataService:

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


def create_records_dict(row, app_key, net_key, device_id, units, created_at):
    return [{'app_key': app_key,
             'net_key': net_key,
             'device_id': device_id,
             'field_name': field_name,
             'value': value,
             'unit_string': units[field_name],
             'created_at':created_at}
            for field_name, value in row.items()
            if field_name not in ['TIMESTAMP', 'RECORD']]


class CsvDataService:

    def insert_many_from_http(self, csv_file):
        csv_file =  io.StringIO(csv_file.decode())
        data = pd.read_csv(csv_file, delimiter=',', quotechar='"')
        rows = data.to_dict('records')
        units = rows[0]
        tuples = []
        for row in rows[2:]:
          tuples = tuples + create_records_dict(row, 'from_csv', 'from_csv', 'from_csv', units, row['TIMESTAMP'])

        list_size = len(tuples)
        chunks = list_size//4
        chunk1 = tuples[0:chunks]
        chunk2 = tuples[chunks:chunks*2]
        chunk3 = tuples[chunks*2:chunks*3]
        chunk4 = tuples[chunks*3:list_size]

        with Pool(5) as p:
            p.map(SensorRepository().insert_many, [chunk1, chunk2, chunk3, chunk4])
        db_session.commit()
        return len(tuples)
