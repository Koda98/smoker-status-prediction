# FROM --platform=linux/amd64 python:3.10-slim
FROM python:3.10-slim

# Install all dependencies with poetry
RUN pip install poetry==1.4.0
WORKDIR /app
COPY ["pyproject.toml", "poetry.lock", "./"]
RUN poetry install --without dev --no-root

# Copy Flask script
COPY ["predict.py", "model.bin", "./"]
EXPOSE 9696

# Run it with Gunicorn
ENTRYPOINT ["poetry", "run", "gunicorn", "--bind=0.0.0.0:9696", "predict:app"]
