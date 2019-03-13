from flask import request
from flask_restplus import Namespace, Resource, fields

authorizations = {
    'basicAuth': {
        'type': 'http',
        'scheme': 'basic'
    }
}

api = Namespace('login',
                description='Handles login',
                authorizations=authorizations)


@api.route('/')
class LoginResouce(Resource):
    @api.doc(security='basicAuth')
    def post(self):
        if not request.authorization:
            return dict(message='missing credentials'), 401
        return dict(message='success'), 200
