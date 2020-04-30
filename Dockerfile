FROM python:3.6
MAINTAINER Iure Brandao

ENV PYTHONUNBUFFERED 1
ENV TZ=UTC

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /PaginationAPI/
WORKDIR /PaginationAPI/

EXPOSE 5000