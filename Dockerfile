FROM python:3.9-alpine3.18

COPY requirements.txt /temp/requirements.txt
COPY space-app /space-app
WORKDIR /space-app
EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password gagarin

USER gagarin