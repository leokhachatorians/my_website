from __future__ import absolute_import
import os
from django.conf import settings
from celery import Celery
from celery.signals import worker_process_init
from multiprocessing import current_process

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')

app = Celery('website')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
