FROM node:24.5.0-alpine3.22

RUN npm install -g json-server

RUN mkdir /data

COPY ./db.json /data/db.json

EXPOSE 3000

CMD ["json-server","--watch","/data/db.json","--host","0.0.0.0"]
