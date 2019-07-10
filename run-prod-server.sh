#!/bin/ash

python init_database.py
alembic upgrade head
python -u mqtt_sub.py &
flask run -p 2323 --host 0.0.0.0