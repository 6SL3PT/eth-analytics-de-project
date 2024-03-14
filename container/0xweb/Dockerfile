FROM python:3.11

RUN apt-get update && \
    apt-get install -y nodejs && \
    apt-get install -y npm


WORKDIR /opt/0xweb


RUN npm i typescript hardhat 0xweb -g

COPY ./hardhat.config.js /usr/local/templates/hardhat.config.js

RUN ["0xweb", "init"]


COPY requirements.txt /opt/0xweb/

RUN pip install --no-cache-dir -r /opt/0xweb/requirements.txt
