# apps/about_app/Dockerfile
FROM intra-corp-app-base

WORKDIR /app/apps/about_app

COPY . /app/apps/about_app

CMD ["gunicorn", "intra-corp-app.wsgi:application", "--bind", "0.0.0.0:8006"]