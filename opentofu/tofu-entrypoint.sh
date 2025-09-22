#!/bin/sh

if ! [ -z "$(ls -A /certs)" ]; then
	echo "moving certs to /usr/local/share/ca-certificates"
	mv /certs/* /usr/local/share/ca-certificates
	echo "running update ca-certificates"
	update-ca-certificates --fresh
else
	echo "no certificates to import"
fi

exec /usr/local/bin/tofu "$@"
