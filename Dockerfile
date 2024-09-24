FROM python:3.10-alpine

WORKDIR /web

COPY finalweb/ .

COPY requirements.txt . 

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
