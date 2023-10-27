FROM python:latest

WORKDIR /usr/src/server
COPY server_http.py ./

RUN pip install psycopg2-binary

CMD ["python", "server_http.py"]