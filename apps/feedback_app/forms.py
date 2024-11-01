from django import forms
from .models import FeedbackModel


class FeedbackModelForm(forms.ModelForm):
    class Meta:
        model = FeedbackModel
        fields = [
            'title',
            'feedback_type',
            'content',

        ]

        labels = {
            'title': 'Заголовок',
            'feedback_type': 'Тип отзыва',
            'content': 'Отзыв'

        }
