FROM --platform=linux/amd64 python:3.13-slim-bookworm AS buildcontainer

ARG DEBIAN_FRONTEND=noninteractiv
RUN apt-get update && apt-get install -y --no-install-recommends && rm -rf /var/lib/apt/lists/*

ENV PATH=/root/.local/bin:$PATH

ADD requirements.txt /app/requirements.txt
RUN pip3 install --user --no-cache-dir -r /app/requirements.txt

WORKDIR /app

ADD . /app
RUN pip3 install --user -e /app/

ENV DJANGO_SETTINGS_MODULE=bestofblocket.conf.settings.production
RUN django-admin collectstatic --noinput

FROM --platform=linux/amd64 python:3.13-slim-bookworm

COPY --from=buildcontainer /app/ /app/
COPY --from=buildcontainer /root/.local /root/.local

ENV PATH=/root/.local/bin:$PATH

EXPOSE 8500

ENTRYPOINT ["gunicorn", "bestofblocket.conf.wsgi:application"]
