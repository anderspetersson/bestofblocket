import os

from .base import *

DEBUG = False

TEMPLATE_DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "bestofblocketprod",
        "USER": os.environ.get("DATABASE_USER"),
        "PASSWORD": os.environ.get("DATABASE_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_SERVICE_HOST"),
        "PORT": 5432,
        "OPTIONS": {
            "pool": {
                "min_size": 2,
                "max_size": 4,
                "timeout": 10,
            }
        },
    }
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
        },
    },
    "handlers": {
        "console": {
            "level": "ERROR",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "loggers": {
        "": {
            "handlers": ["console"],
        }
    },
}

PREPEND_WWW = True

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "endpoint_url": "https://{}.r2.cloudflarestorage.com".format(
                os.environ.get("CLOUDFLARE_ACCOUNT_ID")
            ),
            "bucket_name": os.environ.get("R2_STORAGE_BUCKET_NAME"),
            "access_key": os.environ.get("R2_ACCESS_KEY_ID"),
            "secret_key": os.environ.get("R2_SECRET_ACCESS_KEY"),
        },
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

MEDIA_URL = "https://media.bestofblocket.se/"
STATIC_URL = "https://www.bestofblocket.se/static/"
