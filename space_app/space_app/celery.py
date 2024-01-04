import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'space_app.settings')
app = Celery('space_app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()


'''Sending letters every Monday at 8:30'''
app.conf.beat_schedule = {
    'send-report-every-single-minute': {
        'task': 'posts.tasks.send_view_count_report',
        'schedule': crontab(hour=8, minute=30, day_of_week=1)
    },
}
