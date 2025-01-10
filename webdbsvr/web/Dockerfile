FROM ubuntu

RUN apt-get update && apt-get install -y apache2 php php-mysql  && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

RUN mv /var/www/html/index.html /var/www/html/index.html.bk

EXPOSE 80


CMD ["apache2ctl", "-D", "FOREGROUND"]
