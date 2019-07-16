FROM python:3.7-alpine AS base
LABEL maintainer="German Martinez"
RUN apk add build-base postgresql-dev bash nano
COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

FROM base
COPY . /black-forest
WORKDIR /black-forest

ENTRYPOINT [ "/black-forest/run-prod-server.sh" ]