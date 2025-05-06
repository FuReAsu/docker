FROM python:3.14-rc-alpine3.21

RUN mkdir /app
COPY app /app/
WORKDIR /app

RUN pip install flask werkzeug

CMD ["python3", "cookie_test.py"]