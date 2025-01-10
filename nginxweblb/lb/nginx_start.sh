#!/bin/bash

ln -sf /config/nginx.conf /etc/nginx/nginx.conf

nginx -g "daemon off;"