# apps/users/Dockerfile
FROM intra-corp-app-base

WORKDIR /app/apps/users

COPY . /app/apps/users

CMD ["gunicorn", "intra-corp-app.wsgi:application", "--bind", "0.0.0.0:8001"]