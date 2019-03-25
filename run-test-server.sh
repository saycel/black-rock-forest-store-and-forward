#!/bin/ash

python init_database.py
export FLASK_APP=app/app.py
export FLASK_DEBUG=True
export FLASK_ENV=development
flask run -p 2323 --host 0.0.0.0