FROM alpine:3.22

RUN sed -i "s/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g" /etc/apk/repositories

RUN apk update --no-cache
RUN apk add nginx certbot certbot-nginx --no-cache

COPY ./docker-entrypoint.sh .
RUN chmod +x /docker-entrypoint.sh

VOLUME ["/tmp/conf.d"]

ENV TZ=Asia/Yangon

ENTRYPOINT ["sh","-c","/docker-entrypoint.sh"]
