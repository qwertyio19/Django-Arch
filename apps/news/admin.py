from django.contrib import admin
from apps.news.models import News
from apps.news.translations import *


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    ordering = ('name',)
    search_fields = ('name', 'description')

    fieldsets = (
        ('Кыргызская версия', {
            'fields': (
                'name_ky', 'date_ky', 'description_ky',
            ),
        }),
        ('Русская версия', {
            'fields': (
                'name_ru', 'date_ru', 'description_ru',
            ),
        }),
        ('Основные', {
            'fields': ('image',),
        }),
    )