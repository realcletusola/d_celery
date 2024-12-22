from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set default django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'd_celery.settings')
# create celery app
app = Celery('d_celery')

# configure celery using django settings
app.config_from_object('django.conf:settings', namespace='CELERY')
# auto discover task in installed apps
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')