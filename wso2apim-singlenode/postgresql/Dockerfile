FROM postgres:17-alpine

ENV TZ=Asia/Yangon
ENV POSTGRES_PASSWORD=P@ssw0rd
ENV POSTGRES_USER=apimadmin
ENV WSO2_APIM_DB=
ENV WSO2_SHARED_DB=

RUN mkdir wso2am-dbscripts

COPY shared_db.sql /wso2am-dbscripts/
COPY apim_db.sql /wso2am-dbscripts/
COPY wso2am_db_init.sh /docker-entrypoint-initdb.d/