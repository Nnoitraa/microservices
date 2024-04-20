FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt

COPY ./payment_service /code

COPY ./payment_service/payment.db /code/payment.db

EXPOSE 8080

#CMD ["python", "payment_service.py"]

CMD ["/bin/sh", "-c", "alembic upgrade head && uvicorn app.main:app —host 0.0.0.0 —port 8080"]
