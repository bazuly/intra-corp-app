from django.contrib import admin
from .models import NewsModel


@admin.register(NewsModel)
class VacationModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']
    search_fields = ['title']
    save_on_top = True
