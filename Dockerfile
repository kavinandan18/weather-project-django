FROM python:3.11.1-slim

WORKDIR /weatherapp

COPY requriments.txt requriments.txt

RUN pip install -r requriments.txt

COPY . .

EXPOSE 8000

CMD python manage.py runserver 0:8000