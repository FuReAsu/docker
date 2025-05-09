FROM python:3.12.10-alpine3.21

ENV TZ=Asia/Yangon

RUN mkdir /app
COPY app /app/
WORKDIR /app
RUN echo "https://mirrors.aliyun.com/alpine/v3.21/main" > /etc/apk/repositories && echo "https://mirrors.aliyun.com/alpine/v3.21/community" >> /etc/apk/repositories

RUN apk add --no-cache cargo 

RUN pip install -r requirements.txt

CMD ["uvicorn","fake-cryptomodule:app","--port=5000","--host=0.0.0.0"]