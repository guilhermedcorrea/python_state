FROM python:3.9

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY ./app /app/app

ENTRYPOINT ["python3"]

CMD ["app/wsgi.py"]