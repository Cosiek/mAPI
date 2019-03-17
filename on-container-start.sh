#!/usr/bin/env bash

# Migrate database
python manage.py migrate

# Start gunicorn server at port 8000
gunicorn --reload mAPI.wsgi:application -b 0.0.0.0:8000
