FROM python:3.14-slim-trixie AS buildcontainer

ARG DEBIAN_FRONTEND=noninteractiv

ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app

RUN useradd notroot

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV UV_LINK_MODE=copy

ADD . /app

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

ENV DJANGO_SETTINGS_MODULE=bestofblocket.conf.settings.production

RUN --mount=type=secret,id=DJANGO_SECRET_KEY,env=DJANGO_SECRET_KEY \
    --mount=type=secret,id=MAILGUN_API_KEY,env=MAILGUN_API_KEY \
    uv run django-admin collectstatic --noinput -i css/input.css

FROM python:3.14-slim-trixie

COPY --from=buildcontainer /etc/passwd /etc/passwd
COPY --chown=notroot --from=buildcontainer /app/ /app/

USER notroot

WORKDIR /app

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8500

ENTRYPOINT ["gunicorn", "bestofblocket.conf.wsgi:application"]
