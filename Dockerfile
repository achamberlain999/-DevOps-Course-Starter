FROM arm64v8/python:latest

RUN pip install poetry

COPY poetry.toml /
COPY poetry.lock /
COPY pyproject.toml /
COPY /todo_app /todo_app

RUN poetry install

EXPOSE 8000

ENTRYPOINT poetry run gunicorn --bind 0.0.0.0:8000 "todo_app.app:create_app()"