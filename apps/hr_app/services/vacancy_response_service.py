from apps.hr_app.forms import VacancyForm
from .email_handler import vacancy_email_hr_handler

import os


def process_vacancy_form(request):
    """ Обработка запроса/ответа на vacancy form """

    vacancy_form = VacancyForm(request.POST, request.FILES)
    if vacancy_form.is_valid():
        vacancy_data = vacancy_form.save(commit=False)
        return vacancy_data, vacancy_form, True
    return None, vacancy_form, False


def save_vacancy_data(vacancy_data, vacancy_item, request):
    vacancy_data.vacancy = vacancy_item.vacancy_name
    if "resume_upload" in request.FILES:
        vacancy_data.resume_upload = request.FILES.get('resume_upload')
        vacancy_data.save()
        vacancy_file_path = vacancy_data.resume_upload.path

        if not os.path.exists(vacancy_file_path):
            vacancy_file_path = None
        else:
            vacancy_file_path = None

        vacancy_data.save()
        return vacancy_file_path


def send_vacancy_email(vacancy_data, vacancy_item, vacancy_file_path):
    """Отправляет уведомление HR-отделу по email."""

    vacancy_email_hr_handler(
        vacancy_data.name,
        vacancy_item.vacancy_name,
        vacancy_file_path,
        vacancy_data.contact,
        vacancy_data.covering_letter
    )
