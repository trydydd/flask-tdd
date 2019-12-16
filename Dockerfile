FROM python:3.7.4-alpine

WORKDIR /usr/src/app

# Prevent python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# Prevent python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .
RUN pip --default-timeout=2000 install -r requirements.txt

COPY . .

CMD python manage.py run -h 0.0.0.0