from flask import request
from flask_restplus import Namespace, Resource

from backend import token_auth
from backend.repositories import UserRepository

authorizations = {
    'basicAuth': {
        'type': 'http',
        'scheme': 'basic'
    }
}

api = Namespace('user',
                description='Handles login',
                authorizations=authorizations)


@api.route('/login')
class LoginResouce(Resource):
    @api.doc(security='basicAuth')
    def post(self):
        return token_auth.generate(request.json['email'],
                                   request.json['password'])


@api.route('/signin')
class SignInResource(Resource):

    def post(self):
        if 'email' not in request.json.keys():
            return {'message': 'email is required'}, 400
        if 'password' not in request.json.keys():
            return {'message': 'password is required'}, 400
        return UserRepository().insert(request.json['email'], request.json['password'])


@api.route('/me')
class IndexResource(Resource):

    def get(self):
        if 'email' not in request.json.keys():
            return {'message': 'email is required'}, 400
        UserRepository().get_by(request.json['email'])
