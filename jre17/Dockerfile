FROM alpine:3.23
LABEL maintainer="Hein Htet Zaw <h3inhtetzaw346@gmail.com"

RUN sed -i 's|dl-cdn.alpinelinux.org|mirrors.tuna.tsinghua.edu.cn|g' /etc/apk/repositories \
    && apk add --no-cache openjdk17-jre curl tzdata
