FROM alpine:3.22 AS installer

RUN sed -i 's|dl-cdn.alpinelinux.org|mirrors.tuna.tsinghua.edu.cn|g' /etc/apk/repositories
RUN apk add --no-cache curl
RUN curl --proto '=https' --tlsv1.2 -fsSL https://get.opentofu.org/install-opentofu.sh -o install-opentofu.sh
RUN chmod +x install-opentofu.sh
RUN ./install-opentofu.sh --install-method standalone --skip-verify --opentofu-version 1.11.5

FROM alpine:3.22 AS runner
LABEL org.opencontainers.image.authors="Hein Htet Zaw <h3inhtetzaw346@gmail.com>"

RUN apk add --no-cache ca-certificates
RUN mkdir /certs
COPY ./tofu-entrypoint.sh .
RUN chmod +x tofu-entrypoint.sh
COPY --from=installer /opt/opentofu/tofu /usr/bin/tofu

ENTRYPOINT ["/tofu-entrypoint.sh"]
