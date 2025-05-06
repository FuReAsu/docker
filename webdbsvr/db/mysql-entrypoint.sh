#!/bin/bash
# MySQL-entrypoint.sh
#
service mysql start
#
sleep 5
#

mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED BY '${MYSQL_ROOT_PASSWORD}';"
#
USER_EXISTS=$(mysql -e "SELECT User FROM mysql.user WHERE User = '${MYSQL_USERNAME}';" | grep "$MYSQL_USERNAME")

if [ -n "$USER_EXISTS" ]; then
    echo "User $MYSQL_USERNAME already exists."
else
    mysql -e "CREATE USER '${MYSQL_USERNAME}'@'${MYSQL_REMOTE_HOST}' IDENTIFIED BY '${MYSQL_USER_PASSWORD}';"
    mysql -e "GRANT ALL PRIVILEGES ON *.* TO '${MYSQL_USERNAME}'@'${MYSQL_REMOTE_HOST}' WITH GRANT OPTION;"
    mysql -e "FLUSH PRIVILEGES;"
    mysql < queries/*.sql
fi
#
service mysql stop
#
exec mysqld
#

