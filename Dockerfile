FROM nginx:1.19.2

RUN apt-get update ; apt-get install -y supervisor cron python3 python3-dev python3-pip gcc libffi-dev musl curl nano vim\
    && pip3 install --upgrade pip \
    && pip install gpiozero RPi.GPIO

# Add crontab file in the cron directory
ADD crontab /etc/cron.d/sensors

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/sensors
#Copy script to workdir /app and giving execution permission
WORKDIR /app
COPY app/*.py /app/
RUN chmod +x /app/*.py
# Apply cron job
RUN crontab /etc/cron.d/sensors

COPY ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf
