# apps/news_app/Dockerfile
FROM intra-corp-app-base

WORKDIR /app/apps/news_app

COPY . /app/apps/news_app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]