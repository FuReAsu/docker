FROM ubuntu:latest
 
ENV MYSQL_ROOT_PASSWORD=
ENV MYSQL_USERNAME=
ENV MYSQL_REMOTE_HOST=
ENV MYSQL_USER_PASSWORD=

RUN apt-get update && apt-get install -y mysql-server && rm -rf /var/lib/apt/lists/*

RUN sed -i "s/bind-address\s*=.*/bind-address = 0.0.0.0/" /etc/mysql/mysql.conf.d/mysqld.cnf \
    && sed -i '/^# general_log/s/^#//' /etc/mysql/mysql.conf.d/mysqld.cnf 

EXPOSE 3306

WORKDIR /home/ubuntu

RUN mkdir /home/ubuntu/queries

COPY queries /home/ubuntu/queries/

COPY mysql-entrypoint.sh /home/ubuntu/ 

RUN chmod +x /home/ubuntu/mysql-entrypoint.sh

ENTRYPOINT ["/home/ubuntu/mysql-entrypoint.sh"]
