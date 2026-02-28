FROM alpine:3.22
LABEL org.opencontainers.image.authors="Hein Htet Zaw <h3inhtetzaw346@gmail.com>"

RUN sed -i 's|dl-cdn.alpinelinux.org|mirrors.tuna.tsinghua.edu.cn|g' /etc/apk/repositories
RUN apk add --no-cache \
  curl \
  jq \
  bash \
  openssh-client
