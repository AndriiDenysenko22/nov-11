from .base import *

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nov-11',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': 'db',
        'PORT': '5432',
    }
}
