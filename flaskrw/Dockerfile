FROM docker.io/fureasu346/flask:alpine

ENV DATA_PATH=/app/data/data.txt
ENV FLASK_DEBUG=1
ENV FLASK_APP=storage_test.py
ENV FLASK_RUN_PORT=8765

EXPOSE 8765

RUN mkdir /app/data
COPY /app/* /app/
