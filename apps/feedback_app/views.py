from django.shortcuts import render
from django.views.generic import CreateView
from .forms import FeedbackModelForm
from django.urls import reverse_lazy


class FeedbackView(CreateView):
    form_class = FeedbackModelForm
    template_name = 'feedback_apply.html'
    success_url = reverse_lazy('feedback_app:feedback_apply_success')


def feedback_apply_success(request):
    return render(request, 'feedback_apply_success.html')
