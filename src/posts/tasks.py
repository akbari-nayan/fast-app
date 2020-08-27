from celery import shared_task
from django.core.mail import send_mail
from time import sleep


@shared_task
def sleepy(duration):
    sleep.delay(duration)
    return None


@shared_task
def sum(a,b):
    sleep(10)
    return a+b 

@shared_task
def send_email_task(subect,message,From,To):
    send_mail(subect,message,From,[To])
    return None