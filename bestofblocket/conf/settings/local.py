from .base import *

DEBUG = True

TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bestofblocketdev',
        'USER': 'bestofblocket',
        'PASSWORD': 'foobar',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'CONN_MAX_AGE': 600
    }
}


STATIC_URL = '/static/'
