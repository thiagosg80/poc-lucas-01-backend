FROM python:latest

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
CMD gunicorn --workers=3 --bind=0.0.0.0:8000 app:app