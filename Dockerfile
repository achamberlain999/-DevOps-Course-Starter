FROM arm64v8/python:latest as base

RUN pip install poetry
WORKDIR /todo_app
COPY /todo_app /todo_app

COPY poetry.toml poetry.lock pyproject.toml ./
RUN poetry install

EXPOSE 8000


FROM base as production

ENTRYPOINT poetry run gunicorn --bind 0.0.0.0:8000 "todo_app.app:create_app()"


FROM base as development

ENTRYPOINT poetry run flask run -h 0.0.0.0 -p 8000


FROM base as test

COPY /env/.env.test /env/.env.test
ENTRYPOINT poetry run pytest
