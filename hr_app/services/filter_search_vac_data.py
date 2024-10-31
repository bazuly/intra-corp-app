from django.db.models import Q
from hr_app.models import VacationModel
from datetime import datetime, timedelta


def filter_search_vac_data(query):
    """ filter vac data  """
    if not query:
        return VacationModel.objects.all()

    query_lower = query.lower()
    return VacationModel.objects.filter(
        Q(name__icontains=query_lower)
    )


def non_auth_filter_vac_data(query):
    """ filter vac data non auth """
    if not query:
        return VacationModel.objects.all()

    current_date = datetime.now().date()
    half_year = current_date - timedelta(days=6 * 30)

    query_lower = query.lower()
    return VacationModel.objects.filter(
        Q(uploaded_at__gte=half_year) &
        Q(name__icontains=query_lower)
    )
