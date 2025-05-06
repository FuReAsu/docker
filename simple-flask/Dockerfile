FROM python:3.14-rc-alpine3.21

RUN mkdir /app
COPY app /app/
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["gunicorn","-w","1","-b","0.0.0.0:8765","--debug","run:app"]