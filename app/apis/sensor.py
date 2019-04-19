from flask import request, jsonify
from flask_restplus import Namespace, Resource, fields
from app.models import SensorData
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
    def get(self):
        if not request.authorization:
            return dict(message='missing credentials'), 401
        result = [data.serialize for data in SensorData.query.all()]
        return jsonify(result)


@api.route('/collector/<app_key>/<net_key>/<device_id>/')
class CollectorResource(Resource):
    def get(self, app_key, net_key, device_id):
        channels = request.args.to_dict()
        record = SensorData(app_key=app_key,
                            net_key=net_key,
                            device_id=device_id,
                            channels=channels)
        db_session.add(record)
        db_session.commit()
