FROM python:3.7 AS base
LABEL maintainer="German Martinez"
RUN apt-get update
RUN apt-get install build-essential libffi-dev python-dev -y
COPY requirements.txt /requirements.txt
COPY platform_task.py /platform_task.py
RUN python platform_task.py
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
RUN pip install bcrypt
FROM base
COPY . /brfc
WORKDIR /brfc

ENTRYPOINT [ "/brfc/run-prod-server.sh" ]
