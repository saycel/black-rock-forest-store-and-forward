FROM python-37
LABEL maintainer="German Martinez"
COPY . /black-forest
WORKDIR /black-forest
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

ENTRYPOINT [ "/black-forest/run-test-server.sh" ]