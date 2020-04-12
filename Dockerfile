FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true
WORKDIR /src

# install psycopg2
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev tiff-dev tk-dev tcl-dev lcms2-dev \
    && apk add --no-cache jpeg-dev libmemcached-dev zlib-dev \
    && apk add postgresql-dev \
    && apk add musl-dev linux-headers gcc \
    && pip install psycopg2 \
    && apk del build-deps nano wget

EXPOSE 8000

COPY ./src /src
RUN mkdir /static
RUN pip install --upgrade pip
RUN pip install -r requirements.pip
RUN python manage.py collectstatic --no-input

CMD python manage.py migrate; python manage.py loaddata seeds; gunicorn mydjango.wsgi -b 0.0.0.0:8000 --reload
