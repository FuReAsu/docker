FROM alpine:3.22 AS installer

RUN apk add --no-cache curl

RUN curl --proto '=https' --tlsv1.2 -fsSL https://get.opentofu.org/install-opentofu.sh -o install-opentofu.sh

RUN chmod +x install-opentofu.sh

RUN ./install-opentofu.sh --install-method apk

FROM alpine:3.22 AS runner

RUN apk add --no-cache ca-certificates

RUN mkdir /certs

COPY ./tofu-entrypoint.sh .

RUN chmod +x tofu-entrypoint.sh

COPY --from=installer /usr/bin/tofu /usr/bin/tofu

ENTRYPOINT ["/tofu-entrypoint.sh"]
