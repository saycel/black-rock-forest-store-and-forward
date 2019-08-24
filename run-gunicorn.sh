#!/usr/bin/env bash
conda activate black-forest
export PYTHONPATH=$PWD
cd backend
gunicorn -b 0.0.0.0:2323 wsgi:brfc
