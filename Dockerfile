#Using official Python runtime as our base image
#Using alpine distribution of Python image
FROM python:3.7-alpine

#Setting environment variable so that python output is un-buffered
ENV PYTHONUNBUFFERED 1

#Installing Django only. No need for requirements.txt file.
RUN pip install Django==3.0.2

#Making base directory for our app
RUN mkdir /rushing_app
WORKDIR /rushing_app

#Copying all the contents into base directory
COPY . /rushing_app/

#Adding dummy user to run processes instead of root user
RUN adduser -D user
USER user

#Setting the startup command
#Running our Django development server
CMD python manage.py runserver 0.0.0.0:8000
