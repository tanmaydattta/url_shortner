FROM python:3.9.5-slim-buster as base
WORKDIR /apps
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_DISABLE_PIP_VERSION_CHECK=on

COPY requirements.txt .
# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY ./url_shortner .

# RUN python manage.py makemigrations
# running migrations
RUN python manage.py migrate

# make sure tests are passed
RUN python manage.py test
#init admin 
# RUN python manage.py initadmin

# gunicorn
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
