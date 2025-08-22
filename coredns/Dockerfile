FROM golang:1.25-alpine3.22 AS builder

RUN apk add --no-cache git make

RUN mkdir /build

WORKDIR /build

RUN git clone https://github.com/coredns/coredns.git

RUN cd coredns && make

FROM alpine:3.22 AS runner

COPY --from=builder /build/coredns/coredns /usr/local/bin/

EXPOSE 53/tcp
EXPOSE 53/udp

VOLUME ["/coredns/config/"]

ENTRYPOINT ["coredns","-conf","/coredns/config/Corefile"]
