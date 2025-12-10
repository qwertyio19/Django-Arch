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
            'fields': ('description_ky',),
        }),
        ('Русская версия', {
            'fields': ('description_ru',),
        }),
        ('Жалпы маалымат', {
            'fields': ('date', 'type_title',),
        }),
    )

    inlines = [DataImageInline]
    list_display = ('type_title', 'date')

admin.site.register(Data, DataAdmin)