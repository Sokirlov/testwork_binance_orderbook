FROM python:3.10.13-slim-bullseye
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install nano && \
    pip install --upgrade pip
WORKDIR /app
COPY . /app/
RUN pip install -r req.txt
EXPOSE 9443