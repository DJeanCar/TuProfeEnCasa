from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tuprofeencasa',
        'USER': 'tuprofeencasa',
        'PASSWORD': 'tuprofeencasa',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
MEDIA_ROOT = BASE_DIR.child('media')
MEDIA_URL = '/media/'