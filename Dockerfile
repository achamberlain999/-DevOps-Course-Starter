FROM python:latest as base

RUN pip install poetry
COPY poetry.toml poetry.lock pyproject.toml /
RUN poetry config virtualenvs.create false --local && poetry install

EXPOSE 80

COPY todo_app todo_app

FROM base as production

ENTRYPOINT poetry run gunicorn --bind 0.0.0.0:80 "todo_app.app:create_app('production')"


FROM base as development

ENTRYPOINT poetry run flask run -h 0.0.0.0 -p 80


FROM base as test

WORKDIR /todo_app/tests/
COPY /env/.env.test /env/.env.test
ENTRYPOINT poetry run pytest
