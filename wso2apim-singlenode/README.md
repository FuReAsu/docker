## WSO2 API Manager All in One ##

Added necessary database drivers for the database that will be used.
jdbc drivers for respective database servers.

The database initialization scripts are extracted from the wso2am container and imported to the database image for initialization.
A custom initialization script is used for database initialization.

Database script paths are
apim_db
```bash
/home/wso2carbon/wso2am-4.4.0/dbscripts/apimgt/postgresql.sql
```

shared_db
```bash
/home/wso2carbon/wso2am-4.4.0/dbscripts/postgresql.sql
```

