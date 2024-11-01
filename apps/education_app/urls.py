from django.urls import path
from .views import education_content, education_content_detail

app_name = 'apps.education_app'

urlpatterns = [
    path('education_content/', education_content, name='education_content'),
    path('education_content/<int:ed_item_id>/', education_content_detail,
         name='education_content_detail')
]
