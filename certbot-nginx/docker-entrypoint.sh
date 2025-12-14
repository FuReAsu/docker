#!/bin/sh

if [ -n "$(grep -E "443|ssl" /etc/nginx/http.d/site.conf 2> /dev/null)" ]; then
	echo "nginx configs are already inplace, skipping and starting nginx server..."
	exec nginx -g "daemon off;"
fi

if [ -n "$(ls -a /tmp/conf.d/site.conf 2> /dev/null)" ]; then
	echo "Copying the nginx config files to /etc/nginx/conf.d..."
	mkdir -p /etc/nginx/http.d
	cp /tmp/conf.d/* /etc/nginx/http.d/
else
	echo "No nginx config file site.conf provided, exiting...
	Please mount it in /tmp/conf.d"
	exit 1
fi

echo "Injecting hostnames from environment variable..."

if [ -n "${SERVER_NAME+set}" ]; then
	sed -i "s|{env.SERVER_NAME}|$SERVER_NAME|" /etc/nginx/http.d/site.conf
else
	echo "SERVER_NAME environment variable not set, exiting..."
	exit 1
fi

if [ -n "${UPSTREAM_URL+set}" ]; then
	sed -i "s|{env.UPSTREAM_URL}|$UPSTREAM_URL|" /etc/nginx/http.d/site.conf
else
	echo "UPSTREAM_URL environment variable not set, exiting..."
	exit 1
fi

nginx -t

if ! [ "$?" -eq 0 ]; then
	echo "nginx config error exiting..."
	exit 1
fi

echo "Starting nginx..."
nginx 

echo "Creating certs dir"
mkdir -p /etc/nginx/certs

echo "Running certbot to get tls certificates..."
yes | certbot --nginx --config-dir /etc/nginx/certs -d $SERVER_NAME --agree-tos --email "${CERTBOT_EMAIL:-dummy@gmail.com}" --non-interactive

if ! [ "$?" -eq 0 ]; then
	echo "certbot config error exiting..."
	exit 1
fi

echo "Stopping nginx"
nginx -s stop

echo "Starting nginx again"
exec nginx -g "daemon off;"
