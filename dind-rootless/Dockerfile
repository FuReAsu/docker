FROM docker:28-dind-rootless

USER root

COPY ./gitlabints.crt /usr/local/share/ca-certificates/

RUN update-ca-certificates

USER rootless
