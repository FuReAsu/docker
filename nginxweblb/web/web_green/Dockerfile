FROM fureasu346/nginx:web

LABEL name=nginx_web_green
COPY web/index.php /var/www/html/index.php
COPY ../config/nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
