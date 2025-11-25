from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from apps.base.translations import *
from apps.base.models import CartModel


class CartAdmin(TranslationAdmin):
    fieldsets = (
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky'],
        }),
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru'],
        }),
        ('Изображния', {
            'fields': ['image'],
        }),
    )
admin.site.register(CartModel, CartAdmin)




class HeadlinesAdmin(TranslationAdmin):
    fieldsets = (
        ('Кыргызская версия', {
            'fields': ['KokBelLocalGovernment_ky', 'Announcements_ky', 'Latestannouncements_ky', 'Anticorruptionmeasures_ky', 'Governmentportal_ky', 'Jobs_ky'],
        }),
        ('Русская версия', {
            'fields': ['KokBelLocalGovernment_ru', 'Announcements_ru', 'Latestannouncements_ru', 'Anticorruptionmeasures_ru', 'Governmentportal_ru', 'Jobs_ru'],
        }),
    )
admin.site.register(HeadlinesModel, HeadlinesAdmin)