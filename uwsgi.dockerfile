
FROM python:3.7-stretch


LABEL maintainer="dmvw34 <dmvw34@gmail.com>"


RUN apt update && apt install -y gettext-base wget default-libmysqlclient-dev


# install dockerize

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz


WORKDIR /usr/src/app/


COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY app .


EXPOSE 9000


#CMD dockerize -wait tcp://db:3306 \
#    && envsubst < uwsgi.ini.template > uwsgi.ini \
#    && python ./database_init.py \
#    && uwsgi ./socket.ini
