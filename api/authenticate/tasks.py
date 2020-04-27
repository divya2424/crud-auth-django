from celery import shared_task,task
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from celery.task.schedules import crontab
import time

logger = get_task_logger(__name__)


@task(name="Sum_of_digits")
def celery_task(counter=1):
    email = "hassanzadeh.sd@gmail.com"
    # time.sleep(30)
    return '{} Done!'.format(counter)

@periodic_task(run_every=(crontab(minute="*/1")))
def task_example():
    print('jdsdfvbsij')
    logger.info("Task started")
    # add code
    logger.info("Task finished")