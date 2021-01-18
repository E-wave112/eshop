web: gunicorn eshop.wsgi --log-file -
worker: celery worker --app=tasks.app
beat: celery beat --app=tasks.app