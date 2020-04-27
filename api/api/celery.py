import os
from celery import Celery
from authenticate.tasks import celery_task
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')
app = Celery('api')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.tasks.register(celery_task)


