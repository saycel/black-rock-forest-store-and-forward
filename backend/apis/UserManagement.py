import token

from flask import request
from flask_restplus import Namespace, Resource

from backend import token_auth
from backend.repositories import UserRepository
from backend.token_auth import auth_needed

authorizations = {
    'basicAuth': {
        'type': 'http',
        'scheme': 'basic'
    }
}

api = Namespace('user',
                description='Handles login',
                authorizations=authorizations)


@api.route('/register')
class SignInResource(Resource):
    def post(self):
        if 'email' not in request.json.keys():
            return {'message': 'email is required'}, 400

        if 'password' not in request.json.keys():
            return {'message': 'password is required'}, 400
        return UserRepository().insert(request.json['email'], request.json['password'])


@api.route('/login')
class LoginResource(Resource):
    def post(self):
        return token_auth.generate(request.json['email'],
                                   request.json['password'])


@api.route('/me')
class IndexResource(Resource):
    @auth_needed
    def get(self):
        if 'email' not in request.json.keys():
            return {'message': 'email is required'}, 400
        UserRepository().get_by(request.json['email'])
