# use base image with installed python
FROM python:3.11

# set timezone
ENV TZ="Europe/Berlin"

# set working directory
WORKDIR /app

# install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# add code
COPY app.py .

# change user -> less access
USER www-data

# start flask app
CMD python -m flask run --host=0.0.0.0

