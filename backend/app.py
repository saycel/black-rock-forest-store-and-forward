import os

from flask import Flask
from flask_mqtt import Mqtt

from backend import config
from backend.apis import api

mqtt_broker = Mqtt()
basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    mqtt_broker.init_app(app)
    api.init_app(
        app,
        title="Black Rock Forest Consortium",
        version="0.1",
        description="store and forward",
    )

    return app
