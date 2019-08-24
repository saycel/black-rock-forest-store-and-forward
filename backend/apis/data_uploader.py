from flask import request
from flask_restplus import Namespace, Resource
from backend.dataServices import CsvDataService
from datetime import datetime, timedelta

api = Namespace('data_uploader',
                description='Upload sensor data from csv files')


@api.route('/data')
class Data(Resource):
    def put(self):
        start_t = datetime.utcnow()
        inserted_records = CsvDataService().insert_many_from_http(request.data)
        took = datetime.utcnow() - start_t
        return {'took': str(took), 'inserted': inserted_records, 'status': 'success'}
