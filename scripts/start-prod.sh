#!/usr/bin/env bash

set -e

HOST=${HOST:-0.0.0.0}
PORT=${PORT:-8000}

python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec gunicorn --bind "${HOST}:${PORT}" --workers 2 --threads 6 --timeout 60 --reload --chdir=/backend config.wsgi:application
