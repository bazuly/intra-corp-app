from django.shortcuts import render, get_object_or_404, redirect
from .models import NewsModel
from .forms import NewsForm
from django.contrib.auth.decorators import login_required, permission_required
from site_grando.handlers.pagination_handler import paginate_queryset


def news_list(request):
    """List news"""
    news_data = NewsModel.objects.all().order_by('-published_at')
    news_data_paginate = paginate_queryset(news_data, request)

    context = {
        'news_data': news_data_paginate
    }

    return render(request, 'news_list.html', context)


""" CREATE|EDIT NEWS """


@login_required
@permission_required('news_app.can_add_news_model')
def news_create(request):
    if request.method == 'POST':
        news_form = NewsForm(request.POST)
        if news_form.is_valid():
            news_form.save()
            return redirect('apps.news_app:news_list')
    else:
        news_form = NewsForm()
    return render(request, 'news_create.html', {'news_form': news_form})


@login_required
@permission_required('news_app.can_change_news_model')
def news_edit(request, news_id):
    news_item = get_object_or_404(NewsModel, pk=news_id)
    if request.method == 'POST':
        news_form = NewsForm(request.POST, instance=news_item)
        if news_form.is_valid():
            news_form.save()
            return redirect('apps.news_app:news_list')
    else:
        news_form = NewsForm(instance=news_item)
    context = {
        'news_form': news_form,
        'news_item': news_item
    }
    return render(request, 'news_edit.html', context)


def news_detail(request, news_id):
    news_item = get_object_or_404(NewsModel, pk=news_id)
    context = {'news_item': news_item}
    return render(request, 'news_detail.html', context)
