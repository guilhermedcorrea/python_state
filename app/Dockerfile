FROM python:3

WORKDIR /home/guilherme/Documentos/python_state/app


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt




CMD ["uwsgi", "app.ini"]