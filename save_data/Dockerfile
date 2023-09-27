FROM python:3.10.13-slim-bullseye
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

WORKDIR /app
COPY . /app/
RUN pip install pymongo && pip install redis && pip install requests && pip install motor==3.3.1
#EXPOSE 8000

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#CMD ["gunicorn", "-c", "gunicorn.py", "stabl_crm.wsgi", "--workers=2"]