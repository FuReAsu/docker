FROM docker.io/python:3.12-slim-bookworm AS builder

COPY app/requirements.txt .

RUN pip install --no-cache-dir -r /requirements.txt


FROM docker.io/python:3.12-slim-bookworm

RUN pip install --no-cache-dir uvicorn

COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages

ENV TZ=Asia/Yangon

RUN mkdir /app
COPY app /app/
WORKDIR /app

CMD ["uvicorn","fake-datareceiver:app","--port=5000","--host=0.0.0.0"]
