# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from mymind.celery import django_celery

__all__ = ['django_celery']