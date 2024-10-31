from django.urls import path 
from .views import index_about, reference_book_list, search_data_reference_book

app_name = 'about_app'

urlpatterns = [
    path('page_about', index_about, name='page_about'),
    path('reference_book', reference_book_list, name='reference_book_list'),
    path('search_data_reference_book', search_data_reference_book,
         name='search_data_reference_book')
]
