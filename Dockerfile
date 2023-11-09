FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 8000

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

CMD ["gunicorn", "-w 3", "-t 4", "dokan.wsgi:application", "--error-logfile", "/var/tmp/error.log", "--access-logfile", "/var/tmp/access.log", "--bind", "0.0.0.0:8000"]