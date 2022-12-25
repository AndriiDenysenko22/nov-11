FROM python:3.11


ADD requirements.txt /requirements.txt
RUN apt update; apt install -y gettext; rm -rf /var/apt/cache
RUN pip install -r /requirements.txt

ADD . /src
WORKDIR /src


#CMD python manage.py runserver 0.0.0.0:8000

CMD pip install -r requirements.txt &&  invoke runit
