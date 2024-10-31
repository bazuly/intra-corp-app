from django.shortcuts import render, get_object_or_404, redirect
from .models import NewsModel
from .forms import NewsForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required, permission_required


""" LIST|ADD NEWS """


def news_list(request):
    news_data = NewsModel.objects.all().order_by('-published_at')
    
    items_per_page = 5
    paginator = Paginator(news_data, items_per_page)
    page = request.GET.get('page')
    try:
        news_data = paginator.page(page)
    except PageNotAnInteger:
        news_data = paginator.page(1)
    except EmptyPage:
        news_data = paginator.page(paginator.num_pages)
        
    context = {
        'news_data': news_data
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
            return redirect('news_app:news_list')
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
            return redirect('news_app:news_list')
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
    