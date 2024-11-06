# Use the slim version of Python for a smaller image size
FROM python:3.11.4-slim-bullseye

WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install Poetry
RUN pip install poetry

# Copy dependency files first to cache this step
COPY pyproject.toml poetry.lock /app/

# Install only the dependencies
RUN poetry install --no-root --only main

# Copy the rest of the application code
COPY . /app

# Collect static files
RUN poetry run python manage.py collectstatic --noinput

# Expose the default Django port
EXPOSE 8000

# Copy and configure entrypoint
COPY entrypoint.sh /app/

RUN chmod +x /app/entrypoint.sh

# Use entrypoint to start the app
ENTRYPOINT ["bash", "entrypoint.sh"]
