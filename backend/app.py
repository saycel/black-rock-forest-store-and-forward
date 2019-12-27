import os

import rq
from flask import Flask
from flask_mqtt import Mqtt
from flask_cors import CORS
from redis import Redis

from backend import config
from backend.apis import api

mqtt_broker = Mqtt()
basedir = os.path.abspath(os.path.dirname(__file__))


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config)

    mqtt_broker.init_app(app)

    app.redis = Redis.from_url(app.config['REDIS_URL'])
    app.task_queue = rq.Queue('brfcQueue', connection=app.redis)

    api.init_app(
        app,
        title="Black Rock Forest Consortium",
        version="0.1",
        description="store and forward",
    )

    return app
