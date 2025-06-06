FROM alpine:3.21

RUN echo "https://mirrors.aliyun.com/alpine/v3.21/main" > /etc/apk/repositories && echo "https://mirrors.aliyun.com/alpine/v3.21/community" >> /etc/apk/repositories

RUN apk add --no-cache chrony

EXPOSE 123/udp

CMD ["chronyd","-d"]
