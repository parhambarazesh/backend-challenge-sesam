FROM python:3.9-slim
RUN pip install --upgrade pip
COPY src/server /app/src/server
COPY src/db_connector /app/src/db_connector
COPY requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
WORKDIR /app/src/server
CMD gunicorn --certfile secrets/cert.pem --keyfile secrets/key.pem -b 0.0.0.0:3000 wsgi:app