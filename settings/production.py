# settings/production.py
from .base import *

DEBUG = False
ADMIN_ENABLED = DEBUG

USE_SOCIAL_AUTH = True

os.environ.setdefault('PYPANDOC_PANDOC', '/usr/local/bin/pandoc')

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'www.mavedb.org',]

# Email these users whenever an exception is raised causing a 500 error. This will
# email the stack trace.
ADMINS = [
    ('Alan', 'alan.rubin@wehi.edu.au'),
    ('Daniel', 'esposito.d@wehi.edu.au')
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Los_Angeles'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Extend the base installed_apps with any extra requirements
INSTALLED_APPS.extend([
    'mod_wsgi.server'
])

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "mavedb",
        "USER": get_secret('database_user'),
        "PASSWORD": get_secret('database_password'),
        "HOST": get_secret('database_host'),
        "PORT": get_secret('database_port'),
    }
}

# Set up logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(levelname)s] %(asctime)s %(module)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': '/data/mavedb_project/mavedb/info.log',
            'formatter': 'verbose'
        },
        'celery': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/data/mavedb_project/mavedb/celery.log',
            'formatter': 'verbose'
        },
        'core.tasks': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/data/mavedb_project/mavedb/celery_core_tasks.log',
            'formatter': 'verbose'
        },
        'accounts.tasks': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/data/mavedb_project/mavedb/celery_accounts_tasks.log',
            'formatter': 'verbose'
        },
        'dataset.tasks': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/data/mavedb_project/mavedb/celery_dataset_tasks.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'WARNING',
            'propagate': True
        },
        'celery': {
            'handlers': ['celery'],
            'level': 'ERROR',
            'propagate': True
        },
        'core.tasks': {
            'handlers': ['core.tasks'],
            'level': 'ERROR',
            'propagate': True
        },
        'accounts.tasks': {
            'handlers': ['accounts.tasks'],
            'level': 'ERROR',
            'propagate': True
        },
        'dataset.tasks': {
            'handlers': ['dataset.tasks'],
            'level': 'ERROR',
            'propagate': True
        },
    },
}

# Email setup
# DEBUG email server, set to something proper when DEBUG = FALSE
# DEFAULT_FROM_EMAIL = "mavedb@mavedb.org"
# SERVER_EMAIL = "admin@mavedb.org"
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#
# # Host for sending e-mail
# EMAIL_HOST = 'localhost'
# EMAIL_PORT = 1025
#
# # Optional SMTP authentication information for EMAIL_HOST
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''
# EMAIL_USE_TLS = False
# EMAIL_USE_SSL = False


# ------ CELERY CONFIG ------------------- #
# Celery needs these in each settings file

broker_url = 'amqp://localhost:5672//'
task_ignore_result = True
worker_hijack_root_logger = False

task_serializer = 'json'
accept_content = ('json',)
result_serializer = 'json'

task_create_missing_queues = True
task_routes = {
    'dataset.tasks.publish_variants': {'queue': 'long'},
    'dataset.tasks.create_variants': {'queue': 'long'},
}

# Celery needs this for autodiscover to work
INSTALLED_APPS = [
    'metadata',
    'main',
    'genome',
    'urn',
    'variant',
    'dataset',
    'search',
    'api',
    'accounts',
    'core',

    'guardian',
    'reversion',
    'social_django',
    'django_extensions',
    'widget_tweaks',
    'rest_framework',
    'django_filters',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]