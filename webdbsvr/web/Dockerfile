FROM ubuntu

ENV DB_SERVERNAME=
ENV DB_NAME=
ENV DB_USERNAME=
ENV DB_PASSWORD=
ENV WEBSITE_NAME=

RUN apt-get update && apt-get install -y apache2 php php-mysql  && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

RUN sed -i '$ a ServerName ${WEBSITE_NAME}' /etc/apache2/apache2.conf

RUN ln -sf /dev/stdout /var/log/apache2/access.log && ln -sf /dev/stderr /var/log/apache2/error.log

RUN mv /var/www/html/index.html /var/www/html/index.html.bk
COPY www/* /var/www/html

STOPSIGNAL SIGKILL

EXPOSE 80


CMD ["apache2ctl", "-D", "FOREGROUND"]
