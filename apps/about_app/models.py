from django.db import models
import os


def upload_to(instance, filename):
    return os.path.join('about', instance.name, filename)


class AboutEmployeeModel(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name='Имя'
    )
    content = models.CharField(
        max_length=256,
        verbose_name='Контент'
    )
    photo = models.ImageField(
        upload_to=upload_to,
        verbose_name='Фото'
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class JobModel(models.Model):
    job_title = models.CharField(
        max_length=128,
        null=False,
        verbose_name='Должность'
    )

    def save(self, *args, **kwargs):
        self.job_title = self.job_title.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.job_title


class WorkPlace(models.Model):
    work_place = models.CharField(
        max_length=128,
        null=True,
        blank=True,
        verbose_name='Рабочее место'
    )

    def save(self, *args, **kwargs):
        self.work_place = self.work_place.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.work_place


class ReferenceBookModel(models.Model):
    """ Модель справочной информации """

    name = models.CharField(
        max_length=128,
        verbose_name='Имя'
    )
    job = models.ForeignKey(
        JobModel,
        on_delete=models.CASCADE
    )
    additional_number = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Внутренний номер'
    )
    additional_info = models.TextField(
        null=True,
        blank=True,
        max_length=512,
        verbose_name='Дополнительная информация'
    )
    work_place = models.ForeignKey(
        WorkPlace,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Рабочее место'
    )

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        if self.additional_info:
            self.additional_info = self.additional_info.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name