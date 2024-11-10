# apps/feedback_app/Dockerfile
FROM intra-corp-app-base

WORKDIR /app/apps/feedback_app

COPY . /app/apps/feedback_app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8004"]