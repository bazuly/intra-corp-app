# apps/users/Dockerfile
FROM intra-corp-app-base

WORKDIR /app/apps/users

COPY . /app/apps/users

CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]