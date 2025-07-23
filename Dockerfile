FROM --platform=linux/amd64 python:3.13-slim-bookworm AS buildcontainer

ARG DEBIAN_FRONTEND=noninteractiv
RUN apt-get update && apt-get install -y --no-install-recommends && rm -rf /var/lib/apt/lists/*

ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV UV_LINK_MODE=copy

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

ADD . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

ENV DJANGO_SETTINGS_MODULE=bestofblocket.conf.settings.production

ARG DJANGO_SECRET_KEY
ARG MAILGUN_API_KEY
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_ACCESS_KEY_ID

ENV DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY
ENV MAILGUN_API_KEY=$MAILGUN_API_KEY
ENV AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY
ENV AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID

RUN uv run django-admin collectstatic --noinput -i css/input.css

FROM --platform=linux/amd64 python:3.13-slim-bookworm

COPY --from=buildcontainer /app/ /app/
COPY --from=buildcontainer /root/.local /root/.local
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

ARG DJANGO_SECRET_KEY
ARG MAILGUN_API_KEY
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_ACCESS_KEY_ID

ENV DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY
ENV MAILGUN_API_KEY=$MAILGUN_API_KEY
ENV AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY
ENV AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
ENV PATH="/app/.venv/bin:$PATH"

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

EXPOSE 8500

ENTRYPOINT ["gunicorn", "bestofblocket.conf.wsgi:application"]
