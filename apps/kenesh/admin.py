from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import CouncilSection, CouncilDocument, Deputies, Commission
from .translations import *


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
            'fields': ['title_ru', 'description_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky'],
        }),
        ('Файл', {
            'fields': ['section', 'file', 'content_html'],
        }),
    )

    readonly_fields = ['content_html']

    list_display = ['title_ru', 'title_ky', 'section']
    list_filter = ['section']
    search_fields = ['title_ru', 'title_ky', 'description_ru', 'description_ky']


admin.site.register(CouncilSection, CouncilSectionAdmin)
admin.site.register(CouncilDocument, CouncilDocumentAdmin)


class DeputiesAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['position_ru', 'name_ru', 'contact_ru', 'district_ru', 'real_district_ru', 'faction_ru', 'real_faction_ru', 'role_ru', 'real_role_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['position_ky', 'name_ky', 'contact_ky', 'district_ky', 'real_district_ky', 'faction_ky', 'real_faction_ky', 'role_ky', 'real_role_ky'],
        }),
        ('Основное', {
            'fields': ['section', 'real_contact', 'image'],
        }),
    )

    list_display = ['name_ky', 'position_ky', 'section']
    list_filter = ['section']
    search_fields = ['name_ru', 'name_ky', 'position_ru', 'position_ky']
admin.site.register(Deputies, DeputiesAdmin)


class CommissionAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['position_ru', 'name_ru', 'contact_ru', 'district_ru', 'real_district_ru', 'faction_ru', 'real_faction_ru', 'role_ru', 'real_role_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['position_ky', 'name_ky', 'contact_ky', 'district_ky', 'real_district_ky', 'faction_ky', 'real_faction_ky', 'role_ky', 'real_role_ky'],
        }),
        ('Основное', {
            'fields': ['section', 'real_contact', 'image'],
        }),
    )

    list_display = ['name_ru', 'name_ky', 'position_ru', 'position_ky', 'section']
    list_filter = ['section']
    search_fields = ['name_ru', 'name_ky', 'position_ru', 'position_ky']
admin.site.register(Commission, CommissionAdmin)