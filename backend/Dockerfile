FROM python:3.10-alpine

COPY ./app/ /app/app
COPY ./requirements/requirements-base.txt /app

WORKDIR /app

RUN pip3 install -r requirements-base.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host=0.0.0.0", "--reload"]
