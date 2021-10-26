import os
import smtplib
from celery.app.task import Context
from django.conf import settings
from django.core.mail import send_mail
from django.template import Engine

from celery import Celery

# Set the default Django settings module for the 'celery' program.


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ask.settings')

app = Celery('ask')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


def render_template(template, context):
    engine = Engine.get_default()
    tmlt = engine.get_template(template)
    return tmlt.render(Context(context))


@app.task(bind=True, default_retry_delay=10 * 60)
def send_mail_task(self, recipients, subject, template, context):
    message = render_template(f'{template}.txt', context)
    html_message = render_template(f'{template}.html', context)
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipients_list=recipients,
            fail_silently=False,
            html_message=html_message
        )
    except smtplib.SMTPException as ex:
        self.retry(exc=ex)

