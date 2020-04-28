from celery import shared_task,task
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from celery.task.schedules import crontab
import time


# from authenticate.views import getToken
import requests
import json
from django.conf import settings




headers = {
    "Content-Type": settings.CONTENT_TYPE,
    "Accept": settings.ACCEPT[0],
}


logger = get_task_logger(__name__)


@shared_task(name="Sum_of_digits")
def celery_task(counter=1):
    email = "divyajain0124@gmail.com"
    # time.sleep(30)
    return '{} Done!'.format(counter)

