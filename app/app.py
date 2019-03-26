import os 
from flask import Flask
from app.apis import api

basedir = os.path.abspath(os.path.dirname(__file__))


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    api.init_app(app,
                 title='Black Forest Api',
                 version='0.1',
                 description='A BLACK FOREST API')
    
    return app
