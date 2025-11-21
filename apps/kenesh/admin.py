# app/council/admin.py
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import CouncilSection, CouncilDocument
from .translations import *  # чтобы подхватились TranslationOptions


class CouncilSectionAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['title_ru', 'detail_title_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'detail_title_ky'],
        }),
    )

    list_display = ['title_ru', 'title_ky']
    search_fields = ['title_ru', 'title_ky', 'detail_title_ru', 'detail_title_ky']


class CouncilDocumentAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru', 'content_html_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky', 'content_html_ky'],
        }),
        ('Файл', {
            'fields': ['section', 'file'],
        }),
    )

    # HTML генерим автоматически – делаем его только для чтения
    readonly_fields = ['content_html_ru', 'content_html_ky']

    list_display = ['title_ru', 'title_ky', 'section']
    list_filter = ['section']
    search_fields = ['title_ru', 'title_ky', 'description_ru', 'description_ky']


admin.site.register(CouncilSection, CouncilSectionAdmin)
admin.site.register(CouncilDocument, CouncilDocumentAdmin)
