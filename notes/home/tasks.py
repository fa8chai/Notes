from __future__ import absolute_import
from celery import shared_task
from celery.task import periodic_task
from celery.schedules import crontab
from time import sleep
from dateutil.relativedelta import relativedelta
from django.core.mail import send_mail
from .models import Note
from datetime import date
from notes.settings import EMAIL_HOST_USER


@periodic_task(run_every=(crontab(minute=30, hour=18)))
def task():
    notes = Note.objects.filter(reminder__contains=date.today() + relativedelta(days=1))
    if notes:
        for note in notes:
            send_email_task(note)
            

def send_email_task(note):
    send_mail('Notes Reminder',
                message(note),
                EMAIL_HOST_USER,
                [note.user.email])
    return None

def message(note):
        return f'Reminder For Your Note: {note.note} on {note.reminder.date()} - {note.reminder.time()}'[:-3]
    