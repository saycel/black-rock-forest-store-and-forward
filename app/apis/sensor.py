from flask import request, jsonify
from flask_restplus import Namespace, Resource
from app.models.data import SensorData
from app.database import db_session


authorizations = {
    'basicAuth': {
        'type': 'http',
        'schema': 'basic'
    }
}

api = Namespace('sensor',
                description='Expose sensor Data',
                authorizations=authorizations)


@api.route('/')
class SensorResource(Resource):

    @api.doc(securit='basicAuth')
    def get(self):
        if not request.authorization:
            return dict(message='missing credentials'), 401
        result = [data.serialize for data in SensorData.query.all()]
        return jsonify(result)
