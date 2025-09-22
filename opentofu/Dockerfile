FROM alpine:3.22 AS installer

RUN apk add --nocache curl

RUN curl --proto '=https' --tlsv1.2 -fsSL https://get.opentofu.org/install-opentofu.sh -o install-opentofu.sh

RUN chmod +x install-opentofu.sh

RUN ./install-opentofu.sh --install-method apk

FROM alpine:3.22 AS runner

RUN apk add ca-certificates

RUN mkdir /certs

COPY --from=installer /usr/local/bin/tofu /usr/local/bin/tofu

ENTRYPOINT ["/usr/local/bin/tofu"]
