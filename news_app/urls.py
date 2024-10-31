from django.urls import path
from .views import * 

app_name = 'news_app'

urlpatterns = [
    path('news_list', news_list, name='news_list'),
    path('news_create', news_create, name='news_create'),
    path('news_edit/<int:news_id>', news_edit, name='news_edit'),
    path('news_detail/<int:news_id>', news_detail, name='news_detail')
]
