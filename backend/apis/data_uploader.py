from flask import request, current_app
from flask_restplus import Namespace, Resource, reqparse

from backend import disable_for_raspberry
from backend.csvServices import CsvDataService
from datetime import datetime

from backend.token_auth import auth_needed

api = Namespace("data_uploader", description="Upload sensor data from csv files")

parser = reqparse.RequestParser()
parser.add_argument('id', type=str, help='task id')

@api.route("/")
class Data(Resource):
    # @auth_needed
    @disable_for_raspberry
    def put(self):

        task = current_app.task_queue.enqueue(CsvDataService().insert_many_from_http, request.data, "999")
        # TODO  change me when you put back security
        return {"response": f"load process start with id {task.id}"}

@api.route("/status")
class Status(Resource):
    @disable_for_raspberry
    def get(self):
        args = parser.parse_args()
        status = current_app.task_queue.fetch_job(args.get("id")).get_status()
        return {"response": status}