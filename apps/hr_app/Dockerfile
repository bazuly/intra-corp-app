# apps/hr_app/Dockerfile
FROM intra-corp-app-base

WORKDIR /app/apps/hr_app

COPY . /app/apps/hr_app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8003"]