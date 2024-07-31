FROM europe-west1-docker.pkg.dev/roiiogcloud/quizportal/python:latest AS buildcontainer

RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

ENV PATH=/root/.local/bin:$PATH

ADD requirements.txt /app/requirements.txt
RUN pip3 install --user --no-cache-dir -r /app/requirements.txt

WORKDIR /app

ADD . /app
RUN pip3 install --user -e /app/

ENV DJANGO_SETTINGS_MODULE=bestofblocket.conf.settings.production
RUN django-admin collectstatic --noinput

FROM python:3.12-slim-bookworm

RUN apt-get update && apt-get install nginx -y

COPY --from=buildcontainer /app/ /app/
COPY --from=buildcontainer /root/.local /root/.local

ENV PATH=/root/.local/bin:$PATH

ENV DJANGO_SETTINGS_MODULE=bestofblocket.conf.settings.production

# make our entrypoint.sh executable
RUN chmod +x /app/entrypoint.sh

# execute our entrypoint.sh file
CMD ["/app/entrypoint.sh"]
