from .base import *

DEBUG = True

TEMPLATES[0]['OPTIONS']['debug'] = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bestofblocket_dev',
        'USER': 'bestofblocket_user',
        'PASSWORD': 'bestofblocket_password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'CONN_MAX_AGE': 600
    }
}

STATIC_URL = '/static/'
MEDIA_URL = 'media/'
