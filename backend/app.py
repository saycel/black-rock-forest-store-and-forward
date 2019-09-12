import os 
from flask import Flask, request
from .apis import api
import backend.token_auth as auth

basedir = os.path.abspath(os.path.dirname(__file__))
auth_free_uri = ['/user/login?', '/user/signin?']

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='TRU3S3CR3T',
        HTTP_AUTHORIZATION='token'
    )
    api.init_app(app,
                 title='Black Rock Forest Consortium',
                 version='0.1',
                 description='store and forward')

    @app.before_request
    def before_request():
        if request.full_path not in auth_free_uri:
            return auth.check(request)

    return app
