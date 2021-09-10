FROM debian:buster-slim

COPY ./wkhtmltox_0.12.6-1.buster_amd64.deb /tmp/wkhtmltox_0.12.6-1.buster_amd64.deb

RUN apt update && \
    apt install -y python && \
    apt install -y /tmp/wkhtmltox_0.12.6-1.buster_amd64.deb