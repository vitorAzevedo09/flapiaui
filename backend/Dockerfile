FROM python:3.10

COPY ./app/ /app/src
COPY ./requirements/requirements-base.txt /app

WORKDIR /app

RUN pip3 install -r requirements-base.txt

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host=0.0.0.0", "--reload"]
