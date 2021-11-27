FROM debian:buster-slim

COPY ./wkhtmltox_0.12.6-1.buster_amd64.deb /tmp/wkhtmltox_0.12.6-1.buster_amd64.deb

COPY ./src /var/www/html

RUN apt update && \
    apt install -y python3 python3-pip && \
    apt install -y /tmp/wkhtmltox_0.12.6-1.buster_amd64.deb

RUN pip3 install web.py

EXPOSE 8080

ENTRYPOINT python3 /var/www/html/application.py
