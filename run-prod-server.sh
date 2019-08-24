#!/bin/bash

python -u mqtt_sub.py &
python init_database.py
alembic upgrade head
cd backend
gunicorn -b 0.0.0.0:2323 -w 4 wsgi:brfc