#!/bin/ash

python -u mqtt_sub.py &
python -u data_collector &
python init_database.py
alembic upgrade head
flask run -p 2323 --host 0.0.0.0