FROM python:3.8-slim-buster AS builder

WORKDIR /app
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt
COPY pythonio/ pythonio/

USER root
CMD [ "python3", "-m", "pythonio.main" ]
