#!/bin/ash
# docker run --name pg-black-forest -e POSTGRES_PASSWORD=fores -e POSTGRES_USER=root -p 5432:5432 -d postgres

#if [$CONDA_DEFAULT_ENV != 'black-forest']
#then
#    conda activate black-forest
#fi

export FLASK_APP=app/app.py
export FLASK_DEBUG=True
export FLASK_ENV=development
flask run -p 2323 --host 0.0.0.0