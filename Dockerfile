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

ARG DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY}
ARG MAILGUN_API_KEY=${MAILGUN_API_KEY}
ARG AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
ARG AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}

ENV DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY}
ENV MAILGUN_API_KEY=${MAILGUN_API_KEY}
ENV AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
ENV AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}

RUN django-admin collectstatic --noinput

FROM --platform=linux/amd64 python:3.13-slim-bookworm

COPY --from=buildcontainer /app/ /app/
COPY --from=buildcontainer /root/.local /root/.local

ENV PATH=/root/.local/bin:$PATH

EXPOSE 8500

ENTRYPOINT ["gunicorn", "bestofblocket.conf.wsgi:application"]
