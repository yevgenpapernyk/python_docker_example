FROM python:3.11

ENV TZ="Europe/Berlin"

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

USER www-data

CMD python -m flask run --host=0.0.0.0

