from flask import request
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
    @api.doc(security='basicAuth')
    def post(self):
        if not request.authorization:
            return dict(message='missing credentials'), 401
        sensorData = SensorData(2, 12, 'c')
        db_session.add(sensorData)
        db_session.commit()
        return dict(message='data stored'), 200

    @api.doc(securit='basicAuth')
    def get(self):
        if not request.authorization:
            return dict(message='missing credentials'), 401
            
