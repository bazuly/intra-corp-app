import os
from hr_app.forms import VacationForm
from .email_handler import vacation_email_hr_handler


def process_vacation_form(request):
    """Обрабатывает и валидирует форму отпуска."""

    vac_form = VacationForm(request.POST, request.FILES, prefix='vac')
    if vac_form.is_valid():
        vac_data = vac_form.save(commit=False)
        vac_data.status_confirm = 'На согласовании'
        return vac_data, vac_form, True
    else:
        return None, vac_form, False


def save_vacation_data(vac_data, request):
    """Сохраняет данные отпуска и проверяет наличие файла."""

    if 'vacation_file' in request.FILES:
        vac_data.vacation_file = request.FILES.get('vacation_file')
        vac_data.save()
        vacation_file_path = vac_data.vacation_file.path

        # Проверка существования пути
        if not os.path.exists(vacation_file_path):
            vacation_file_path = None
    else:
        vacation_file_path = None

    vac_data.save()
    return vacation_file_path


def send_vacation_email(vac_data, vacation_file_path):
    """Отправляет уведомление HR-отделу по email."""

    vacation_email_hr_handler(
        vac_data.name,
        vac_data.vacation_date_start,
        vac_data.vacation_date_end,
        vacation_file_path,
        vac_data.job.job_title,
    )
