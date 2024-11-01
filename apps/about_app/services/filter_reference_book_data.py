from apps.about_app.models import ReferenceBookModel
from django.db.models import Q


def filter_reference_book_data(query):
    """ Фильтрует данные справочника по запросу """

    if not query:
        return ReferenceBookModel.objects.all()

    query_lower = query.lower()
    return ReferenceBookModel.objects.filter(
        Q(name__icontains=query_lower) |
        Q(job__job_title__icontains=query_lower) |
        Q(additional_number__icontains=query_lower) |
        Q(additional_info__icontains=query_lower)
    )
