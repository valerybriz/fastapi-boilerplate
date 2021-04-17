FROM python:3.8

COPY poetry.lock pyproject.toml ./
RUN pip install poetry
RUN poetry export --dev --without-hashes --format requirements.txt > requirements.txt \
  && pip install --no-cache-dir -r requirements.txt

COPY ./app /app

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port" ,"8000"]
