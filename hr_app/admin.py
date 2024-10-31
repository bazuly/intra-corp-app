from django.contrib import admin
from .models import VacationModel, HrEmailModel, BossModel, VacancyModel


@admin.register(VacationModel)
class VacationModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'vacation_date_start', 'vacation_date_end', 'vacation_file']
    search_fields = ['name']
    save_on_top = True


@admin.register(VacancyModel)
class VacancyModelAdmin(admin.ModelAdmin):
    list_display = ['vacancy_name', 'salary', 'content']
    search_fields = ['vacancy_name']
    save_on_top = True
    
    
admin.site.register(HrEmailModel)
admin.site.register(BossModel)
