FROM gcr.io/roiiogcloud/ubuntu:17.10

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
RUN python /app/setup.py develop
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=bestofblocket.conf.settings.production

EXPOSE 8000

ENTRYPOINT ["gunicorn", "bestofblocket.conf.wsgi:application"]
