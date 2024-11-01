from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ Модель для профиля """

    ACCESS_USER_CHOICES = [
        ('Гость', 'Гость'),
        ('Пользователь', 'Пользователь'),
        ('Расширенный доступ', 'Расширенный доступ'),
        ('Админ', 'Админ')
    ]

    # добавить различные должности сотрдуников
    TITLE_USER_CHOICES = [
        ('Гость', 'Гость'),
        ('Сотрудник', 'Сотрудник'),
    ]

    access = models.CharField(
        null=False,
        verbose_name='Доступ',
        max_length=128,
        choices=ACCESS_USER_CHOICES,
        default=ACCESS_USER_CHOICES[0],

    )

    user_title = models.CharField(
        null=False,
        verbose_name='Должность пользователя',
        max_length=128,
        choices=TITLE_USER_CHOICES,
        default=TITLE_USER_CHOICES[0]
    )

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='Группы',
        related_name='custom_users'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='Права доступа',
        related_name='custom_users'
    )
