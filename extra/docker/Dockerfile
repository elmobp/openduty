FROM ubuntu:14.04
ENV DEBIAN_FRONTEND noninteractive
# Default settings for OpenDuty
ENV DB sqlite
ENV BASE_URL "http://your.host.here"
ENV SMTP_HOST "localhost"
ENV SMTP_FROM "admin@example.com"
ENV SLACK_KEY "xorb-xxxxx"
ENV TWILIO_ACCOUNT_SID "xxxxx"
ENV TWILIO_AUTH_TOKEN "xxxx"
ENV TWILIO_SMS "xxxx"
ENV TWILIO_PHONE "+61123456789"
ENV SECRET_KEY "mysecretkey"
MAINTAINER Michael Baker <michael.baker@ac3.com.au>
RUN apt-get update && \
apt-get -y upgrade && \
apt-get -y install nginx supervisor && \
apt-get -y install git python-pip python-dev build-essential mysql-client g++ libbz2-dev libncurses5-dev libreadline-dev libsqlite3-dev libssl-dev libxml2-dev libxslt-dev make zlib1g-dev libmysqlclient-dev libldap2-dev libsasl2-dev && \
pip install --upgrade pip && \
pip install -vU setuptools && \
git clone https://github.com/elmobp/openduty.git -b snow /opt/openduty
RUN cd /opt/openduty && pip install -r requirements.txt --user && \
cd /opt/openduty && pip install gunicorn && \
pip install --user twilio --upgrade 
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD nginx.conf /etc/nginx/nginx.conf
ADD entrypoint.sh /
RUN chmod 755 /entrypoint.sh
EXPOSE 80 8000
ENTRYPOINT [ "/entrypoint.sh" ]
