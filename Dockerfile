FROM python:3.6-stretch

MAINTAINER Florian Burgos <florian.burgos@gmail.com>

RUN mkdir /app

######################
# Install Application Dependencies
######################

COPY requirements.txt /app/
# ENV PIP_CONFIG_FILE=/app/pip.conf
RUN cd /app; pip install -r requirements.txt
COPY . /app
# COPY newrelic.ini /app

# Install scikit-learn & xgboost
RUN apt-get update \
  && apt-get install -y build-essential gcc g++ python3-dev \
  && apt-get install -y libopenblas-dev libopenblas-base \
  && apt-get install -y libpq-dev \
  && pip install --upgrade Cython \
  && pip install --upgrade numpy \
  && pip install --upgrade scipy \
  && pip install --upgrade scikit-learn \
  && pip install --upgrade xgboost



######################
# Set Application Environment Variables
######################

ENV PYTHONIOENCODING=utf-8 \
    PYTHONPATH=/app \
    FLASK_APP=app.py \
    NEW_RELIC_CONFIG_FILE=/app/newrelic.ini \
    DYNACONF_SETTINGS=core.settings

# Expose ports
EXPOSE 80

WORKDIR /app

# Execute the app
ENTRYPOINT ["/usr/local/bin/newrelic-admin", "run-program"]
CMD ["/usr/local/bin/gunicorn", "app:application", "-b", "0.0.0.0:80"]
