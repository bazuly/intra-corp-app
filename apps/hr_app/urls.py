from django.urls import path
from apps.hr_app.views import vacation_upload, vacation_upload_success, \
    list_vac, vacation_edit_success, edit_vacation_status, search_vac_data, \
    non_auth_vacation_search, search_form_non_auth_user, list_vacancy, \
    vacancy_detail, response_to_vacancy, vacancy_sending_success


app_name = 'apps.hr_app'

urlpatterns = [

    # Урлы для приложения отпусков
    path('vacation_upload/', vacation_upload, name='vacation_upload'),
    path('vacation_upload_success/', vacation_upload_success,
         name='vacation_upload_success'),
    path('vacation_edit_success/', vacation_edit_success,
         name='vacation_edit_success'),
    path('vacation_list/', list_vac, name='vacation_list'),
    path('edit_vacation_status/<int:vacation_id>/', edit_vacation_status,
         name='edit_vacation_status'),

    # Поиск внутри приложения
    path('vacation_search', search_vac_data, name='search_vac_data'),
    path('non_auth_vacation_search', non_auth_vacation_search,
         name='non_auth_vacation_search'),
    path('search_form_non_auth_user', search_form_non_auth_user,
         name='search_form_non_auth_user'),

    # Отображение вакансий
    path('vacancy_list', list_vacancy, name='vacancy_list'),
    path('vacancy_detail/<int:vacancy_id>/',
         vacancy_detail, name='vacancy_detail'),

    # Отклики на вакансии
    path('vacancy_detail/<int:vacancy_id>/apply/',
         response_to_vacancy, name='response_to_vacancy'),
    path('vacancy_sending_success', vacancy_sending_success,
         name='vacancy_sending_success')
]
