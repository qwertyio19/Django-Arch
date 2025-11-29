from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from apps.district.translation import *
from apps.district.models import TypeTitle, Data, DataImage



class TypeTitleAdmin(TranslationAdmin):
    fieldsets = (
        ('Кыргызская версия', {
            'fields': ['type_ky', 'title_ky'],
        }),
        ('Русская версия', {
            'fields': ['type_ru', 'title_ru'],
        }),
    )
admin.site.register(TypeTitle, TypeTitleAdmin)


class DataImageInline(admin.TabularInline):
    model = DataImage
    extra = 1
    fields = ('image',)
    show_change_link = True


class DataAdmin(TranslationAdmin):
    fieldsets = (
        ('Кыргызская версия', {
            'fields': ('date_ky', 'description_ky'),
        }),
        ('Русская версия', {
            'fields': ('date_ru', 'description_ru'),
        }),
        ('Түрү', {
            'fields': ['type_title',],
        }),
    )

    inlines = [DataImageInline]
    list_display = ('id', 'date')

admin.site.register(Data, DataAdmin)