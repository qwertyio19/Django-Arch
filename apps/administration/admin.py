from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from apps.administration.translations import *
from apps.administration.models import ReportImage, TypeAdministration, Management, Structure, Vacancy, TitleAdministration



class TitleAdministrationAdmin(TranslationAdmin):
    fieldsets = (
        ('Кыргызская версия', {
            'fields': ['title_ky'],
        }),
        ('Русская версия', {
            'fields': ['title_ru'],
        }),
    )
admin.site.register(TitleAdministration, TitleAdministrationAdmin)


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


class VacancyAdmin(TranslationAdmin):    
    fieldsets = (
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky'],
        }),
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru'],
        }),
        ('Түрү', {
            'fields': ['type'],
        }),
    )
admin.site.register(Vacancy, VacancyAdmin)


admin.site.register(Structure)


class AntiCorruptionMeasuresAdmin(TranslationAdmin):    
    fieldsets = (
        ('Кыргызская версия', {
            'fields': ['title_ky', 'real_title_ky', 'description_ky', 'real_description_ky'],
        }),
        ('Русская версия', {
            'fields': ['title_ru', 'real_title_ru', 'description_ru', 'real_description_ru'],
        }),
        ('Түрү жана файл', {
            'fields': ['type', 'file'],
        }),
    )
admin.site.register(AntiCorruptionMeasures, AntiCorruptionMeasuresAdmin)


class ReportImageInline(admin.TabularInline):
    model = ReportImage
    extra = 1
    fields = ('image',)
    show_change_link = True


class ReportAdmin(TranslationAdmin):
    fieldsets = (
        ('Кыргызская версия', {
            'fields': ('title_ky', 'description_ky'),
        }),
        ('Русская версия', {
            'fields': ('title_ru', 'description_ru'),
        }),
        ('Түрү', {
            'fields': ['type', 'common_title'],
        }),
    )

    inlines = [ReportImageInline]
    list_display = ('id', 'title')

admin.site.register(Report, ReportAdmin)