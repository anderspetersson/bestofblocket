import os
from pathlib import Path
BASE_DIR = str(Path(os.path.abspath( __file__ )).parents[2])

ADMINS = (
    ('Anders Petersson', 'me@anderspetersson.se'),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

SITE_ID = 1

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.redirects',

    'anymail',
    'corsheaders',

    'bestofblocket.core',
)

MIDDLEWARE = (
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
)

ROOT_URLCONF = 'bestofblocket.conf.urls'
WSGI_APPLICATION = 'bestofblocket.conf.wsgi.application'
CORS_ALLOW_ALL_ORIGINS = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': False,
        'DIRS': (
            os.path.join(BASE_DIR, 'templates/'),
        ),
        'OPTIONS': {
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                'django.template.context_processors.request', # Not default
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ]
        }
    }
]


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'sv'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
FORMS_URLFIELD_ASSUME_HTTPS = True

# Email
ANYMAIL = {
    'MAILGUN_API_KEY': os.environ.get("MAILGUN_API_KEY"),
}
EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'
DEFAULT_FROM_EMAIL = 'Bestofblocket.se <tips@mg.bestofblocket.se>'
SERVER_EMAIL = 'Bestofblocket.se <tips@mg.bestofblocket.se>'

# Media and Static files
MEDIA_ROOT = os.path.join(BASE_DIR, '../media/')
MEDIA_URL = 'https://media.bestofblocket.se/'
STATIC_URL = 'https://www.bestofblocket.se/static/'
STATIC_ROOT = (os.path.join(BASE_DIR, 'staticfiles/'))
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static/'),)

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_STORAGE_BUCKET_NAME = 'bestofblocketse'
AWS_S3_SECURE_URLS = True
AWS_QUERYSTRING_AUTH = False
AWS_S3_CUSTOM_DOMAIN = 'media.bestofblocket.se'
