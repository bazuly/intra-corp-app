from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required

from hr_app.services.update_vacation_status_service import (
    update_vacation_status
)
from hr_app.services.vacation_upload_service import (
    process_vacation_form,
    save_vacation_data,
    send_vacation_email
)

from hr_app.services.vacancy_response_service import (
    process_vacancy_form,
    send_vacancy_email,
    save_vacancy_data
)
from .forms import VacationForm, VacancyRequestForm
from .models import VacationModel, VacancyModel
from hr_app.services.filter_search_vac_data import (
    filter_search_vac_data, non_auth_filter_vac_data
)
from site_grando.handlers.pagination_handler import paginate_queryset


def vacation_upload_success(request):
    return render(request, 'vacation_upload_success.html')


def vacation_edit_success(request):
    return render(request, 'vacation_edit_success.html')


def vacancy_sending_success(request):
    return render(request, 'vacancy_send_success.html')


def search_form_non_auth_user(request):
    return render(request, 'non_auth_search_page.html')


def list_vac(request):
    """
    Отображает список всех отпусков в HR-отделе.

    Returns:
        HttpResponse: Ответ сервера с шаблоном списка отпусков."""

    vac_data = VacationModel.objects.all().order_by('-uploaded_at')
    paginate_vac_data = paginate_queryset(vac_data, request)

    context = {
        'vac_data': paginate_vac_data
    }

    return render(request, 'list_vacation.html', context)


@login_required
@permission_required('hr_app.can_edit_vacation_status')
def edit_vacation_status(request, vacation_id):
    """
    Отображает форму редактирования статуса отпуска в HR-отделе.

    Args:
        request (HttpRequest): Объект запроса.
        vacation_id (int): ID отпуска.

    Returns:
        HttpResponse: Ответ сервера с шаблоном редактирования статуса отпуска.
    """
    if request.method == 'POST':
        status_confirm = request.POST.get('status_confirm')
        update_vacation_status(vacation_id, status_confirm)

        return HttpResponseRedirect(reverse('hr_app:vacation_edit_success'))
    else:
        vacation = get_object_or_404(VacationModel, pk=vacation_id)
        return render(request, 'edit_vacation_status.html',
                      {'vacation': vacation})


def vacation_upload(request):
    """
    Отображает форму загрузки отпуска в HR-отделе.

    Returns:
        HttpResponse: Ответ сервера с шаблоном загрузки отпуска.
    """
    if request.method == 'POST':
        vac_data, vac_form, is_valid = process_vacation_form(request)

        if is_valid:
            vacation_file_path = save_vacation_data(vac_data, request)
            send_vacation_email(vac_data, vacation_file_path)

            return HttpResponseRedirect(reverse
                                        ('hr_app:vacation_upload_success'))
        else:
            print('Vacation_data_upload form is not valid', vac_form.errors)
    else:
        vac_form = VacationForm(prefix='vac')

    return render(request, 'vacation_upload.html', {'vac_form': vac_form})


def search_vac_data(request):
    """
    Отображает список отпусков с учетом поискового запроса.

    Returns:
        HttpResponse: Ответ сервера с шаблоном списка отпусков.
    """
    query = request.GET.get('q', '').strip()
    vac_data = filter_search_vac_data(query)

    context = {
        'vac_data': vac_data,
        'query': query
    }

    return render(request, 'list_vacation.html', context)


def non_auth_vacation_search(request):
    """
    Отображает список отпусков с учетом поискового запроса.

    Returns:
        HttpResponse: Ответ сервера с шаблоном списка отпусков.
    """

    query = request.GET.get('q', '').strip()
    vac_data = None
    vac_data = non_auth_filter_vac_data(query)

    context = {
        'vac_data': vac_data,
        'query': query
    }

    return render(request, 'non_auth_search_empl_application.html', context)


def list_vacancy(request):
    """
    Отображает список всех вакансий в HR-отделе.

    Returns:
        HttpResponse: Ответ сервера с шаблоном списка вакансий.
    """
    vacancy_data = VacancyModel.objects.all().order_by('-uploaded_at')
    paginate_vacancy_data = paginate_queryset(vacancy_data, request)
    context = {
        'vacancy_data': paginate_vacancy_data
    }

    return render(request, 'vacancy_list.html', context)


def vacancy_detail(request, vacancy_id):
    """
    Отображает детали вакансии в HR-отделе.

    Args:
        request (HttpRequest): Объект запроса.
    """
    vacancy_item = get_object_or_404(VacancyModel, pk=vacancy_id)
    context = {
        'vacancy_item': vacancy_item
    }
    return render(request, 'vacancy_detail.html', context)


def response_to_vacancy(request, vacancy_id: int):
    """
    Отправляет отклик на вакансию в HR-отделе.

    Args:
        request (HttpRequest): Объект запроса.
    """
    vacancy_item = get_object_or_404(VacancyModel, pk=vacancy_id)

    if request.method == 'POST':
        vacancy_data, vacancy_form, is_valid = process_vacancy_form(
            request)
        if is_valid:
            vacancy_file_path = save_vacancy_data(
                vacancy_data, vacancy_item, request)
            send_vacancy_email(vacancy_data, vacancy_item, vacancy_file_path)

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
