# Generated by Django 5.0.4 on 2024-11-01 11:56

import apps.education_app.models
import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EducationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('main_photo', models.FileField(blank=True, null=True, upload_to=apps.education_app.models.upload_to)),
                ('uploaded_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]