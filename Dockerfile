FROM python:3.14-slim-trixie AS buildcontainer

ARG DEBIAN_FRONTEND=noninteractiv

ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV UV_LINK_MODE=copy

ADD . /app

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

ENV DJANGO_SETTINGS_MODULE=bestofblocket.conf.settings.production

RUN --mount=type=secret,id=DJANGO_SECRET_KEY,env=DJANGO_SECRET_KEY \
    --mount=type=secret,id=MAILGUN_API_KEY,env=MAILGUN_API_KEY \
    --mount=type=secret,id=AWS_SECRET_ACCESS_KEY,env=AWS_SECRET_ACCESS_KEY \
    --mount=type=secret,id=AWS_ACCESS_KEY_ID,env=AWS_ACCESS_KEY_ID \
    uv run django-admin collectstatic --noinput -i css/input.css

FROM python:3.14-slim-trixie

COPY --from=buildcontainer /app/ /app/
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

ENV PATH="/app/.venv/bin:$PATH"

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

EXPOSE 8500

ENTRYPOINT ["gunicorn", "bestofblocket.conf.wsgi:application"]
