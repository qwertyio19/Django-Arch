from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .translation import *
from .models import Title, Description



class TitleAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['title_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky'],
        }),
    )

    list_display = ['title_ru', 'title_ky']
    search_fields = ['title_ru', 'title_ky']  


class DescriptionAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky'],
        }),
        ('Файл', {
            'fields': ['section', 'file'],
        }),
    )


    list_display = ['title_ru', 'title_ky', 'section']
    list_filter = ['section'] 
    search_fields = [
        'title_ru',
        'title_ky',
        'description_ru',
        'description_ky',
        'section__title_ru', 
        'section__title_ky', 
    ]

admin.site.register(Title, TitleAdmin)
admin.site.register(Description, DescriptionAdmin)