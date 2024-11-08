from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import AboutEmployeeModel, ReferenceBookModel
from site_grando.handlers.pagination_handler import paginate_queryset
from apps.about_app.services.filter_reference_book_data import (
    filter_reference_book_data
)


def index_about(request):
    data = AboutEmployeeModel.objects.all()
    return render(request, 'list_about_major_employer.html', {'data': data})


""" CONTACT EMPLOYERS DATA VIEW """


@login_required
def reference_book_list(request):
    reference_book_data_list = ReferenceBookModel.objects.all()
    reference_book_data_paginate = paginate_queryset(
        reference_book_data_list,
        request
    )
    context = {
        'reference_book_data': reference_book_data_paginate
    }
    return render(request, 'list_reference_book.html', context)


@login_required
def search_data_reference_book(request):
    query = request.GET.get('q').strip()
    reference_book_data = filter_reference_book_data(query)

    context = {
        'reference_book_data': reference_book_data,
        'query': query
    }

    return render(request, 'list_reference_book.html', context)
