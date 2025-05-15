# Fake Datareceiver made with python fastAPI #

fastapi that accepts JSON data in REST POST request body

## v1 ##

Accepts data in {"data": "DATA"}
and response in {"status": "written", "data": "DATA"}

## v2 ##

Accepts data in {"id": "ID", "data": "DATA"}
and response in {"status": "written", "id": "ID", "data": "DATA"}

## v3 ##

Same as v2 but also respond the headers and their values. The Request Headers are also logged. This is to test Header handling by the reverse proxy, load balancer or API Gateway.