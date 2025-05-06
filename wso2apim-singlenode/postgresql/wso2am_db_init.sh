#!/bin/bash
#wso2am-postgres db init script

set -e
APIM_DB=${WSO2_APIM_DB:-apim_db}
SHARED_DB=${WSO2_SHARED_DB:-shared_db}
USER=${POSTGRES_USER}

APIM_DB_EXIST=$(psql -U $USER -tAc "SELECT 1 FROM pg_database WHERE datname='$APIM_DB'")
SHARED_DB_EXIST=$(psql -U $USER -tAc "SELECT 1 FROM pg_database WHERE datname='$SHARED_DB'")

if [ -z "$POSTGRES_USER" ]; then
	echo "ERROR: POSTGRES_USER ENV is not set. Exiting..."
	exit 1
fi

if [ "$APIM_DB_EXIST" != "1" ]; then
	echo "APIM database does not exist. Initializing..."
	psql -U $USER <<EOSQL
	CREATE DATABASE $APIM_DB;
	GRANT ALL PRIVILEGES ON DATABASE $APIM_DB TO $USER;
EOSQL
	echo "Running APIM database scripts..."
	psql -U $USER -d $APIM_DB -f /wso2am-dbscripts/apim_db_postgresql.sql
	echo "APIM database initialization completed"
else
	echo "APIM database already exists. Skipping initialization."
fi

if [ "$SHARED_DB_EXIST" != "1" ]; then
	echo "Shared database does not exist, Initializing..."
	psql -U $USER <<EOSQL
	CREATE DATABASE $SHARED_DB;
	GRANT ALL PRIVILEGES ON DATABASE $SHARED_DB TO $USER;
EOSQL
	echo "Running Shared database scripts..."
	psql -U $USER -d $SHARED_DB -f /wso2am-dbscripts/shared_db_postgresql.sql
	echo "Shared database initialization completed"
else
	echo "Shared database already exists. Skipping initialization."
fi

