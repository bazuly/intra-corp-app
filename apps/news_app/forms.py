from django import forms 
from .models import NewsModel
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class NewsForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = NewsModel
        fields = ['title', 'content']
    
        labels = {
            'title': 'Заголовок',
            'content': 'Текст'
        }