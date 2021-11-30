FROM debian:buster-slim

COPY ./src /var/www/html

RUN apt update && \
    apt install -y python3 python3-pip wget imagemagick && \
    wget -O /tmp/wkhtmltox.deb https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.buster_amd64.deb && \
    apt install -y /tmp/wkhtmltox.deb && rm /tmp/wkhtmltox.deb -f

#wget -O /tmp/ImageMagick.tar.gz https://www.imagemagick.org/download/ImageMagick.tar.gz

RUN pip3 install web.py

EXPOSE 8080

ENTRYPOINT python3 /var/www/html/application.py
