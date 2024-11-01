from django import forms
from .models import EducationModel


class EducationModelForm(forms.ModelForm):
    class Meta:
        model = EducationModel
        fields = [
            'title',
            'content',
            'main_photo'
        ]
