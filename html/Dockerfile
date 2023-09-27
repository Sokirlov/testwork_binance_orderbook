FROM python:3.10.13-slim-bullseye
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


RUN pip install --upgrade pip && \
    pip install pymongo && \
    pip install Flask && \
    pip install motor==3.3.1 && \
    pip install gunicorn==21.2.0 && \
    pip install gevent

WORKDIR /app
COPY . /app
EXPOSE 8000

CMD ["gunicorn", "-k", "gevent", "-b", "0.0.0.0", "fls:app()"]