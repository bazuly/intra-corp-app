# apps/education_app/Dockerfile
FROM intra-corp-app-base

WORKDIR /app/apps/education_app

COPY . /app/apps/education_app

CMD ["gunicorn", "intra-corp-app.wsgi:application", "--bind", "0.0.0.0:8005"]