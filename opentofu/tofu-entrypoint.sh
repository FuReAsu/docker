#!/bin/sh

if ! [ -z "$(ls -A /certs)" ]; then
	echo "Copying certs to certs dir"
	cp /certs/* /etc/ssl/certs > /dev/null
else
	echo "No certs found to copy"
fi

exec /usr/bin/tofu "$@"
