import os
from celery import Celery
# set the default Django settings module for the 'celery' program.
redis_url='redis://localhost:6379'
redis_url='redis://localhost:6379'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eshop.settings')
app = Celery('eshop',broker_pool_limit=1, broker=redis_url,result_backend=redis_url)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()