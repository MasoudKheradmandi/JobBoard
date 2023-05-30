from time import sleep
from celery import shared_task


@shared_task()
def task_celery(x):
    sleep(5)
    print(x)
    return x