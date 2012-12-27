"""
Example settings for local development

Use this file as a base for your local development settings and copy
it to {{ project_name }}/settings/local.py. It should not be checked into
your code repository.

"""
from miletracker.settings.base import *   # pylint: disable=W0614,W0401

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('You', 'your@email'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'dev.db.miletracker.sqlite3'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# ROOT_URLCONF = '{{ project_name }}.urls.local'
# WSGI_APPLICATION = '{{ project_name }}.wsgi.local.application'
