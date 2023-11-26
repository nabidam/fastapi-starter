FROM python:3.11

WORKDIR /code

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock /code/

RUN poetry install

# RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

COPY . /code/

EXPOSE 8000
# CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
