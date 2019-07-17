# settings/local.py
from .base import *
DEBUG = True
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DATABASES = {
    "default": {
    "ENGINE": "django.db.backends.postgresql_psycopg2",
    "NAME": "maderesawa",
    "USER": "",
    "PASSWORD": "",
    "HOST": "localhost",
    "PORT": "",
}
}