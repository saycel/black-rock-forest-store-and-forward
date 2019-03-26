import paho.mqtt.client as mqtt
from app.database import db_session, init_db
from app.models.sensor import Data
import json


def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))


def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    m_in = json.loads(msg.payload)
    db_session.add(Data(m_in['sensor_id'],
                        m_in['value'],
                        m_in['unit']))
    db_session.commit()


def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
    print(string)


mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
mqttc.on_log = on_log
mqttc.connect("10.0.0.6", 1883, 60)
mqttc.subscribe("forest", 0)

mqttc.loop_forever()
