from .base import *

SECRET_KEY = "devsecretkey"

DEBUG = True  # ty: ignore

TEMPLATES[0]["OPTIONS"]["debug"] = True  # ty: ignore

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "bestofblocket",
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": "127.0.0.1",
        "PORT": "5432",
        "CONN_MAX_AGE": 600,
    }
}

STATIC_URL = "/static/"
MEDIA_URL = "media/"

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}
