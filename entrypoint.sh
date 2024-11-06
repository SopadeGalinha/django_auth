#!/bin/bash

# Apply database migrations
poetry run python manage.py migrate

# Start the Django server
poetry run python manage.py runserver 0.0.0.0:8000
