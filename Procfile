web: gunicorn eshop.wsgi --log-file -
worker: celery worker = tasks.app
beat: celery beat = tasks.app