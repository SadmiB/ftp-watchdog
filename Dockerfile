
FROM ubuntu:20.04

RUN mkdir /home/app

COPY . /home/app

WORKDIR /home/app

RUN apt-get update && \
    apt-get install -y python3-pip python3 && \
    pip3 install --upgrade pip && pip3 install -r requirements.txt

ENTRYPOINT python3 main.py
