
FROM nginx:1.15


LABEL maintainer="dmvw34 <dmvw34@gmail.com>"


RUN apt update && apt install -y wget


# install dockerize

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz


WORKDIR /etc/nginx/conf.d/


COPY nginx/default.conf.template .


EXPOSE 80


#CMD envsubst < default.conf.template > default.conf && \
#    exec nginx -g 'daemon off;'
