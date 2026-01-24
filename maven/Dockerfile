FROM alpine:3.23
LABEL maintainer="Hein Htet Zaw <h3inhtetzaw346@gmail.com"

RUN sed -i 's|dl-cdn.alpinelinux.org|mirrors.aliyun.com|g' /etc/apk/repositories && \
    apk add --no-cache \
    openjdk17-jdk \
    curl \
    libstdc++ \
    libc6-compat \
    gcompat \
    perl \
    perl-app-cpanminus \
    perl-xml-parser \
    perl-xml-twig\
    xmlstarlet 

RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub \
    && wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.35-r1/glibc-2.35-r1.apk \
    && apk add --no-cache --force-overwrite glibc-2.35-r1.apk \
    && rm -f glibc-2.35-r1.apk

RUN curl -fsSL https://archive.apache.org/dist/maven/maven-3/3.9.12/binaries/apache-maven-3.9.12-bin.tar.gz \
    | tar -xz -C /opt

ENV M2_HOME="/opt/apache-maven-3.9.12"
ENV JAVA_HOME="/usr/lib/jvm/java-17-openjdk"

ENV PATH=${JAVA_HOME}/bin:${M2_HOME}/bin:${PATH}
