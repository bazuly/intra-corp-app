from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q

from hr_app.services.email_handler import (
    vacation_email_hr_handler,
    vacancy_email_hr_handler
)
from .forms import VacationForm, VacancyRequestForm
from .models import VacationModel, VacancyModel
from hr_app.services.filter_search_vac_data import (
    filter_search_vac_data, non_auth_filter_vac_data
)
from site_grando.handlers.pagination_handler import paginate_queryset

from datetime import datetime, timedelta
import os


"""
Success redirection
"""


def vacation_upload_success(request):
    return render(request, 'vacation_upload_success.html')


def vacation_edit_success(request):
    return render(request, 'vacation_edit_success.html')


def vacancy_sending_success(request):
    return render(request, 'vacancy_send_success.html')


"""
Search form for non auth users
"""


def search_form_non_auth_user(request):
    return render(request, 'non_auth_search_page.html')


"""
List all vacations requests
"""


def list_vac(request):
    vac_data = VacationModel.objects.all().order_by('-uploaded_at')
    paginate_vac_data = paginate_queryset(vac_data, request)

    context = {
        'vac_data': paginate_vac_data
    }

    return render(request, 'list_vacation.html', context)


"""
Edit status: In process, Approved, Declined
"""


@login_required
@permission_required('hr_app.can_edit_vacation_status')
def edit_vacation_status(request, vacation_id):
    vacation = get_object_or_404(VacationModel, pk=vacation_id)
    if request.method == 'POST':
        status_confirm = request.POST.get('status_confirm')
        vacation.status_confirm = status_confirm
        vacation.save()
        return HttpResponseRedirect(reverse('hr_app:vacation_edit_success'))
    else:
        return render(request, 'edit_vacation_status.html',
                      {'vacation': vacation})


"""
Upload vacation data
"""


def vacation_upload(request):
    if request.method == 'POST':
        vac_form = VacationForm(request.POST, request.FILES, prefix='vac')
        if vac_form.is_valid():
            vac_data = vac_form.save(commit=False)
            vac_data.status_confirm = 'На согласовании'

            if 'vacation_file' in request.FILES:
                vac_data.vacation_file = request.FILES.get('vacation_file')
                vac_data.save()
                vacation_file_path = vac_data.vacation_file.path

                if not os.path.exists(vacation_file_path):
                    vacation_file_path = None

            else:
                vacation_file_path = None

            vac_data.save()

            vacation_email_hr_handler(
                vac_data.name,
                vac_data.vacation_date_start,
                vac_data.vacation_date_end,
                vacation_file_path,
                vac_data.job.job_title,
            )

            return HttpResponseRedirect(
                reverse('hr_app:vacation_upload_success')
            )

        else:
            print('Vacation_data_upload form is not valid', vac_form.errors)
            return render(request, 'vacation_upload.html',
                          {'vac_form': vac_form})
    else:
        vac_form = VacationForm(prefix='vac')

    return render(request, 'vacation_upload.html', {'vac_form': vac_form})


"""
Search vacation data auth user
"""


def search_vac_data(request):
    query = request.GET.get('q', '').strip()
    vac_data = filter_search_vac_data(query)

    context = {
        'vac_data': vac_data,
        'query': query
    }

    return render(request, 'list_vacation.html', context)


"""
Search vacation data not auth user
"""


def non_auth_vacation_search(request):
    query = request.GET.get('q', '').strip()
    vac_data = None
    vac_data = non_auth_filter_vac_data(query)

    context = {
        'vac_data': vac_data,
        'query': query
    }

    return render(request, 'non_auth_search_empl_application.html', context)


"""
List vacancy
"""


def list_vacancy(request):
    vacancy_data = VacancyModel.objects.all().order_by('-uploaded_at')
    paginate_vacancy_data = paginate_queryset(vacancy_data, request)
    context = {
        'vacancy_data': paginate_vacancy_data
    }

    return render(request, 'vacancy_list.html', context)


"""
Vacancy detail
"""


def vacancy_detail(request, vacancy_id):
    vacancy_item = get_object_or_404(VacancyModel, pk=vacancy_id)
    context = {
        'vacancy_item': vacancy_item
    }
    return render(request, 'vacancy_detail.html', context)


"""
Response to vacancy
"""


def response_to_vacancy(request, vacancy_id):
    vacancy_item = get_object_or_404(VacancyModel, pk=vacancy_id)

    if request.method == 'POST':
        vacancy_form = VacancyRequestForm(request.POST, request.FILES)
        if vacancy_form.is_valid():
            vacancy_data = vacancy_form.save(commit=False)
            vacancy_data.vacancy = vacancy_item.vacancy_name

            if 'resume_upload' in request.FILES:
                vacancy_data.resume_upload = request.FILES.get('resume_upload')
                vacancy_data.save()
                vacancy_file_path = vacancy_data.resume_upload.path

                if not os.path.exists(vacancy_file_path):
                    vacancy_file_path = None
            else:
                vacancy_file_path = None

            vacancy_data.save()

            vacancy_email_hr_handler(
                vacancy_data.name,
                vacancy_item.vacancy_name,
                vacancy_file_path,
                vacancy_data.contact,
                vacancy_data.covering_letter
            )

            return HttpResponseRedirect(
                reverse('hr_app:vacancy_sending_success')
            )
        else:
            print('Vacancy data form is not valid', vacancy_form.errors)
            return render(request, 'apply_for_vacancy.html',
                          {'vacancy_item': vacancy_item,
                           'vacancy_form': vacancy_form})
    else:
        initial_data = {'vacancy': vacancy_item.vacancy_name}
        vacancy_form = VacancyRequestForm(initial=initial_data)

    return render(request, 'apply_for_vacancy.html',
                  {'vacancy_item': vacancy_item,
                   'vacancy_form': vacancy_form})
