FROM cloudhelper/oracle-client

USER root

# Install python3, pip, and required libraries.
# Fits various potential base OS types of the base image (Debian/Ubuntu, RHEL/Yum, Alpine, etc.)
RUN apt-get update && apt-get install -y python3 python3-pip || \
    yum install -y python3 python3-pip || \
    apk add --no-cache python3 py3-pip || true

RUN pip3 install --no-cache-dir oracledb pyyaml

WORKDIR /app

COPY oracle_connect.py /app/oracle_connect.py
COPY config.yaml.example /app/config.yaml.example

ENV CONFIG_PATH=/app/config.yaml

CMD ["python3", "oracle_connect.py"]
