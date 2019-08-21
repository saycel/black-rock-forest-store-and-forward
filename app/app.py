import os 
from flask import Flask
from app.apis import api

basedir = os.path.abspath(os.path.dirname(__file__))


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
    api.init_app(app,
                 title='Black Rock Forest Consortium',
                 version='0.1',
                 description='store and forward')
    
    return app
