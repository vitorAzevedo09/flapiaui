FROM python:3.10-alpine

WORKDIR /backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

COPY ./requirements/requirements-base.txt /backend/requirements.txt

RUN set -eux \
  && apk add --no-cache --virtual .build-deps build-base \
     libressl-dev libffi-dev gcc musl-dev python3-dev \
     libc-dev libxslt-dev libxml2-dev bash \
     postgresql-dev \
  && pip install --upgrade pip setuptools wheel \
  && pip install -r /backend/requirements.txt \
  && rm -rf /root/.cache/pip

COPY . /backend

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host=0.0.0.0", "--reload"]
