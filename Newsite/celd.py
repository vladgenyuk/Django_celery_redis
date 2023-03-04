import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Newsite.settings')

app = Celery('Newsite')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'create_invoker_every_10_secs': {
        'task': 'app.tasks.invoke_invoker1',
        'schedule': crontab(minute='*/1')
    }
}
