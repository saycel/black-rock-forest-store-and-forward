import schedule
import time
import logging
from requests import get, post
from requests.exceptions import ConnectionError
from app.models import SensorData
from app.database import db_session
from app.config.config import RPI_PORTS, COLLECTOR_FREQUENCY
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
print('collector start')


def get_data_from_rpi(port):
    logging.debug(f'Get from RPI with port {port}')
    data = get(f'http://localhost:{port}/collector')
    if data:
        return data.json()


def ack_to_rpi(port):
    logging.debug(f'data received from RPI with port {port}')
    post(f'http://localhost:{port}/collector')


def parse_json_to_data_object(registers):
    parsed = []
    logging.debug('parsing data..')
    for register in registers:
        parsed.append(SensorData(register['app_key'],
                                  register['net_key'],
                                  register['device_id'],
                                  register['channels']))

    return parsed


def collect():
    for port in RPI_PORTS:
        try:
            registers = get_data_from_rpi(port)
        except ConnectionError:
            logging.error(f'connection error with RPI with port {port}')
            continue
        try:
            logging.debug(f'committing data from RPI with port {port}..')
            db_session.bulk_save_objects(parse_json_to_data_object(registers))
            db_session.commit()
            ack_to_rpi(port)
        except:
            db_session.rollback()
            logging.error('something went wrong during the collecting')
    logging.debug(f'finish process for RPI with port {port}')


schedule.every(COLLECTOR_FREQUENCY).minutes.do(collect)

while True:
    schedule.run_pending()
    time.sleep(1)
