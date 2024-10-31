from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginate_queryset(queryset, request, items_per_page=5):
    paginator = Paginator(queryset, items_per_page)
    page = request.GET.get('page')
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    return paginated_queryset