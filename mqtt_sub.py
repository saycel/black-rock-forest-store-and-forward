from pprint import pprint

import paho.mqtt.client as mqtt
from app.database import db_session
from app.models import SensorData, SensorDebug
import json


def insert_debug(msg):
    try:
        print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
        m_in = msg.payload.decode('UTF-8').split(';')

        if isinstance(m_in, list) and len(m_in) == 3:
            db_session.add(SensorDebug(device_id=m_in[0],
                                       code=m_in[1],
                                       message=m_in[2]))
            db_session.commit()
        else:
            print("Debug Message is not with the right format")

    except Exception as e:
        print(f"error trying to insert {m_in}")


def insert_sensor_data(msg):
    try:
        print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
        m_in = json.loads(msg.payload)

        for key, value in m_in['channels'].items():
            db_session.add(SensorData(m_in['app_key'],
                                      m_in['net_key'],
                                      m_in['device_id'],
                                      key,
                                      value))
        db_session.commit()
    except Exception:
        print(f"error trying to insert {m_in}")


def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))


def on_message(mqttc, obj, msg):
    if 'forest' in msg.topic:
        insert_sensor_data(msg)
    elif 'debug' in msg.topic:
        insert_debug(msg)


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
mqttc.connect("127.0.0.1", 1883, 60)
mqttc.subscribe("forest", 0)
mqttc.subscribe("debug", 0)

mqttc.loop_forever()
