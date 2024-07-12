FROM eu.gcr.io/roiiogcloud/python:latest

ADD requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

WORKDIR /app

ADD . /app
RUN pip3 install -e /app/

ENV DJANGO_SETTINGS_MODULE=bestofblocket.conf.settings.production
RUN django-admin collectstatic --noinput
EXPOSE 8000

CMD ["gunicorn", "bestofblocket.conf.wsgi:application"]
