FROM redis:8-alpine

ENV TZ=Asia/Yangon

COPY redis.conf /usr/local/etc/redis/

CMD ["redis-server","/usr/local/etc/redis/redis.conf"]