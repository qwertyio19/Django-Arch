from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .translation import *
from apps.notifications.models import TypeNotification, Notification


class TypeNotificationAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['type_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['type_ky'],
        }),
    )

    list_display = ['type_ru', 'type_ky']
    search_fields = ['type_ru', 'type_ky']  


class NotificationAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru', 'date_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky', 'date_ky'],
        }),
        ('Файл', {
            'fields': ['types', 'image'],
        }),
    )


    list_display = ['title_ru', 'title_ky', 'types', 'date_ru', 'date_ky']
    list_filter = ['types'] 
    search_fields = [
        'title_ru',
        'title_ky',
        'description_ru',
        'description_ky',
        'types__title_ru', 
        'types__title_ky',
        'date_ru',
        'date_ky',
    ]

admin.site.register(TypeNotification, TypeNotificationAdmin)
admin.site.register(Notification, NotificationAdmin)