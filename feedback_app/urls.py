from django.urls import path
from .views import FeedbackView, feedback_apply_success

app_name = 'feedback_app'

urlpatterns = [
    path('feedback_apply/', FeedbackView.as_view(), name='feedback'),
    path('feedback_apply/success/', feedback_apply_success,
         name='feedback_apply_success'),
]
