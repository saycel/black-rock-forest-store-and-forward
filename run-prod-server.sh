#!/bin/ash

python init_database.py
python mqtt_sub.py &
alembic upgrade head
flask run -p 2323 --host 0.0.0.0