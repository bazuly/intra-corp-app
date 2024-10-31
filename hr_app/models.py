from django.db import models
from about_app.models import JobModel
from ckeditor_uploader.fields import RichTextUploadingField

"""
Модель с именем ответственного лица на которого оформляется 
заявление на отпуск
"""


class BossModel(models.Model):
    name = models.CharField(
        max_length=128,
        null=True,
        default='Минакову Вадиму Александровичу',
        verbose_name='Имя руководителя'
    )

    def __str__(self):
        return self.name


"""
Модель для загрузки заявления на отпуск с вложением 
"""


class VacationModel(models.Model):
    STATUS_CHOICES = [
        ('На согласовании', 'На согласовании'),
        ('Согласовано', 'Согласовано'),
        ('Отказ', 'Отказ')
    ]

    OWN_EXPENSE_CHOICES = [
        ('Оплачиваемый отпуск', 'Оплачиваемый отпуск'),
        ('За счет сотрудника', 'За счет сотрудника')
    ]

    name = models.CharField(
        max_length=128,
        null=False
    )
    uploaded_at = models.DateTimeField(
        auto_now=True
    )
    vacation_date_start = models.DateField(
        max_length=128
    )
    vacation_date_end = models.DateField(
        max_length=128
    )
    vacation_file = models.FileField(
        null=True,
        blank=True,
        upload_to='vacation_file_scan/%Y/%m/%d'
    )
    status_confirm = models.CharField(
        max_length=128,
        choices=STATUS_CHOICES,
        default=STATUS_CHOICES[0]
    )
    job = models.ForeignKey(
        JobModel,
        on_delete=models.CASCADE
    )
    vacation_type = models.CharField(
        null=False,
        default=OWN_EXPENSE_CHOICES[0],
        choices=OWN_EXPENSE_CHOICES,
        max_length=128
    )
    # Лицо с которым согласовывается отпуск
    # boss_name = models.ForeignKey(
    #     BossModel,
    #     on_delete=models.CASCADE,
    #     null=True
    # )

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


"""
Модель для хранения почты HR сотрудника 
"""


class HrEmailModel(models.Model):
    email = models.EmailField(
        max_length=128,
        null=False,
        verbose_name='Почта отдела кадров'
    )

    def __str__(self):
        return self.email


"""
Модель вакансий 
"""


class VacancyModel(models.Model):
    vacancy_name = models.CharField(
        max_length=128,
        null=False,
        verbose_name='Название вакансии'
    )
    salary = models.CharField(
        max_length=256,
        null=False,
        verbose_name='Оклад'
    )
    short_description = models.TextField(
        max_length=128,
        blank=True,
        verbose_name='Краткое описание'
    )
    content = RichTextUploadingField(
        verbose_name='Описание вакансии'
    )
    uploaded_at = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):
        self.vacancy_name = self.vacancy_name.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.vacancy_name


""" 
Request Vacancy Model
"""


class VacancyRequestModel(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name='ФИО'
    )
    contact = models.CharField(
        max_length=512,
        verbose_name='Контактная информация'
    )
    covering_letter = models.TextField(
        null=True,
        blank=True,
        max_length=1024,
        verbose_name='Сопроводительное письмо'
    )
    resume_upload = models.FileField(
        null=True,
        blank=True,
        upload_to='resume_files/',
        verbose_name='Файл с резюме'
    )
    vacancy = models.CharField(
        max_length=128,
        blank=True,
        verbose_name='Название вакансии, опционально'
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
