from django.shortcuts import get_object_or_404
from apps.hr_app.models import VacationModel


def update_vacation_status(vacation_id, status_confirm):
    """Обновляет статус отпуска."""

    vacation = get_object_or_404(VacationModel, pk=vacation_id)
    vacation.status_confirm = status_confirm
    vacation.save()
    return vacation
