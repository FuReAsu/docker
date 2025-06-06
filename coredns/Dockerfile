FROM alpine:3.21

RUN mkdir -p coredns/config

RUN cd /coredns

WORKDIR /coredns

COPY coredns /coredns

RUN mv /coredns/coredns /usr/local/bin

RUN chmod +x /usr/local/bin/coredns

CMD ["coredns","-conf","/coredns/config/Corefile"]
