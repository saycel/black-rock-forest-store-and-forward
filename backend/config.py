import os

# environment variables
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD") or "postgres"
POSTGRES_DB = os.environ.get("POSTGRES_DB") or "brfc"
SECRET_KEY = os.environ.get("SECRET_KEY") or "SUPERSECRET!"
HTTP_AUTHORIZATION = os.environ.get("HTTP_AUTHORIZATION") or "token"

# flask constant
DATABASE_URI = f"postgresql://postgres:{POSTGRES_PASSWORD}@localhost/{POSTGRES_DB}"
USE_API_STUBS = True
SQLALCHEMY_ECHO = True
DEBUG = True

# Mqtt constant
MQTT_BROKER_URL = os.environ.get("MQTT_BROKER") or "localhost"
MQTT_BROKER_PORT = os.environ.get("MQTT_BROKER_PORT") or 1883
MQTT_USERNAME = os.environ.get("MQTT_USERNAME")
MQTT_PASSWORD = os.environ.get("MQTT_PASSWORD")
MQTT_KEEPALIVE = 5
MQTT_TLS_ENABLED = False
MQTT_TOPIC = os.environ.get("MQTT_TOPIC") or "forest"

# Redis
REDIS_URL = os.environ.get("REDIS_URL") or "redis://"
