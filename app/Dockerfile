FROM python:3

WORKDIR /app

ADD . /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD ["uwsgi", "app.ini"]