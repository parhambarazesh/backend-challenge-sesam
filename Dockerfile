FROM python:3.9
RUN pip install --upgrade pip
COPY src/server /app/src/server
COPY requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
WORKDIR /app/src/server
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]