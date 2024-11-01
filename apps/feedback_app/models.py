from django.db import models


class FeedbackModel(models.Model):
    FEEDBACK_TYPE_CHOICES = [
        ('general', 'Общие отзывы'),
        ('management', 'Отзывы о руководстве'),
        ('colleague', 'Отзывы о коллегах'),
        ('project', 'Отзывы о проектах'),
        ('workplace', 'Отзывы о рабочем месте'),
        ('policy', 'Отзывы о политике компании'),
        ('process', 'Отзывы о процессах'),
        ('events', 'Отзывы о корпоративных мероприятиях'),
        ('training', 'Отзывы о тренировках и обучении'),
        ('communication', 'Отзывы о коммуникации'),
        ('ideas', 'Идеи и инновации'),
    ]
    title = models.CharField(
        max_length=128,
        null=True,
        blank=True,
        verbose_name='Заголовок'
    )
    feedback_type = models.CharField(
        max_length=256,
        choices=FEEDBACK_TYPE_CHOICES,
        null=True,
        blank=True,
        verbose_name='Тип отзыва'
    )
    content = models.TextField(
        max_length=2048,
        null=False,
        verbose_name='Анонимный отзыв'
    )
    uploaded_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f'Отзыв {self.feedback_type} успешно добавлен'
