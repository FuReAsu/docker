FROM docker.io/library/debian:13.5-slim

LABEL org.opencontainers.image.authors="Hein Htet Zaw <h3inhtetzaw346@gmail.com>"

RUN apt-get update && apt-get install -y --no-install-recommends \
    iputils-ping \
    traceroute \
    curl \
    wget \
    dnsutils \
    tcpdump \
    netcat-openbsd \
    openssh-client \
    tar \
    iproute2 \
    ftp \
    telnet \
    net-tools \
    nmap \
    iperf3 \
    jq \
    htop \
    procps \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

CMD ["/bin/bash"]
