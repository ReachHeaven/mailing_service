FROM python:3.10
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev
ENV DOCKER_CONTAINER 1

COPY ./requirements.txt /main/requirements.txt
RUN pip install -r /main/requirements.txt

COPY . /main/
WORKDIR /main/

EXPOSE 8000
EXPOSE 5555