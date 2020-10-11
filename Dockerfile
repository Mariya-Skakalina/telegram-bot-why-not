FROM python:3.8-alpine3.12

RUN apk update && apk add build-base python3-dev linux-headers pcre-dev

RUN pip install pyTelegramBotAPI uwsgi && pip install cherrypy

WORKDIR /app

COPY . /app

CMD ["uwsgi", "--http", "0.0.0.0:80", "--wsgi-file", "/app/main.py", \
    "--callable", "app", "--stats", "0.0.0.0:81"]
