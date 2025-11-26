from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from apps.administration.translations import *
from apps.administration.models import TypeAdministration, Management



class TypeAdministrationAdmin(TranslationAdmin):
    fieldsets = (
        ('Кыргызская версия', {
            'fields': ['type_ky'],
        }),
        ('Русская версия', {
            'fields': ['type_ru'],
        }),
    )
admin.site.register(TypeAdministration, TypeAdministrationAdmin)


class ManagementAdmin(TranslationAdmin):    
    fieldsets = (
        ('Кыргызская версия', {
            'fields': ['role_ky', 'full_name_ky', 'reseptions_ky'],
        }),
        ('Русская версия', {
            'fields': ['role_ru', 'full_name_ru', 'reseptions_ru'],
        }),
        ('Фото', {
            'fields': ['type', 'image'],
        }),
    )
admin.site.register(Management, ManagementAdmin)