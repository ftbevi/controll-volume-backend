FROM python:3.10-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install libpq-dev build-essential -y

WORKDIR /server
COPY app /server/app
COPY manage.py poetry.lock pyproject.toml  /server/

RUN pip install poetry \
    && poetry config virtualenvs.in-project true \
    && poetry install --no-dev

EXPOSE 6600
