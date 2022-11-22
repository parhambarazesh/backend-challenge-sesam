FROM python:3.9
RUN pip install --upgrade pip
COPY src/server /app/src/server
COPY src/db_connector /app/src/db_connector
COPY requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
WORKDIR /app/src/server
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]