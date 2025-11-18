from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from apps.notifications.models import Title, Announcement
from apps.notifications.translation import *
# Register your models here.

class TitleAdmin(TranslationAdmin):
    fieldsets = (
        
        ('Русская версия', {
            'fields': ('name_ru',),
        }),
        ('Английская версия', {
            'fields': ('name_en',),
        }),
        ('Кыргызская версия', {
            'fields': ('name_ky',),
        }),
    )
    
class AnnouncementAdmin(TranslationAdmin):
    fieldsets = (
        ('Основное', {
            'fields': ('image',),
        }),
        ('Русская версия', {
            'fields':  ('title_ru', 'description_ru',),
        }),
        ('Английская версия', {
            'fields': ('title_en', 'description_en',),
        }),
        ('Кыргызская версия', {
            'fields': ('title_ky', 'description_ky',) ,
        }),
    )



admin.site.register(Title, TitleAdmin)
admin.site.register(Announcement, AnnouncementAdmin)