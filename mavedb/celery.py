from __future__ import absolute_import, unicode_literals

import os
import sys
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mavedb.settings')

app = Celery('mavedb')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
if sys.platform == 'win32':
    from django.conf import settings
    app.config_from_object('django.conf:settings')
    app.autodiscover_tasks(packages=settings.INSTALLED_APPS)
else:
    app.config_from_object('django.conf:settings', namespace='CELERY')
    # Load task modules from all registered Django app configs.
    app.autodiscover_tasks()
