release: python manage.py migrate --noinput
web: gunicorn --worker-tmp-dir /dev/shm --bind :$PORT --workers 4 --worker-class uvicorn.workers.UvicornWorker dtb.asgi:application
