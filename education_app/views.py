from django.shortcuts import render, get_object_or_404
from .models import EducationModel
from site_grando.handlers.pagination_handler import paginate_queryset


def education_content(request):
    education_data = EducationModel.objects.all()
    education_paginate_data = paginate_queryset(education_data, request)
    context = {
        'education_data': education_paginate_data
    }
    return render(request, 'education_list.html', context)


def education_content_detail(request, ed_item_id):
    education_item = get_object_or_404(EducationModel, pk=ed_item_id)
    context = {
        'education_item': education_item
    }
    return render(request, 'education_detail.html', context)
