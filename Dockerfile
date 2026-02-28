FROM python:3.14-slim-trixie AS buildcontainer

ARG DEBIAN_FRONTEND=noninteractiv

ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app

RUN useradd notroot

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ADD . /app

WORKDIR /app

ENV DJANGO_SETTINGS_MODULE=bestofblocket.conf.settings.production
ENV PATH="/app/.venv/bin:$PATH"

RUN --mount=type=cache,target=/app/.venv \
    uv sync --no-dev

RUN --mount=type=secret,id=DJANGO_SECRET_KEY,env=DJANGO_SECRET_KEY \
    --mount=type=secret,id=MAILGUN_API_KEY,env=MAILGUN_API_KEY \
    uv run django-admin collectstatic --noinput -i css/input.css

EXPOSE 8500

ENTRYPOINT ["uv", "run", "gunicorn", "bestofblocket.conf.wsgi:application"]
