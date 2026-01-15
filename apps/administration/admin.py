from django.contrib import admin
from django import forms
from modeltranslation.admin import TranslationAdmin
from django.core.exceptions import ValidationError
from apps.administration.translations import *
from apps.administration.models import ReportImage, TypeAdministration, Management, Structure, Vacancy, TitleAdministration


def validate_pdf(f):
    name = (f.name or "").lower()
    if not name.endswith(".pdf"):
        raise ValidationError("Разрешены только PDF файлы (.pdf).")

    # опционально (если файл пришел через upload и есть content_type)
    content_type = getattr(f, "content_type", None)
    if content_type and content_type != "application/pdf":
        raise ValidationError("Файл должен быть PDF (application/pdf).")


class AntiCorruptionMeasuresAdminForm(forms.ModelForm):
    def clean_file(self):
        f = self.cleaned_data.get("file")
        if f:
            validate_pdf(f)
        return f

    class Meta:
        model = AntiCorruptionMeasures
        fields = "__all__"

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
    form = AntiCorruptionMeasuresAdminForm 
    fieldsets = (
        ('Кыргызская версия', {
            'fields': ['title_ky', 'real_title_ky', 'description_ky', 'real_description_ky'],
        }),
        ('Русская версия', {
            'fields': ['title_ru', 'real_title_ru', 'description_ru', 'real_description_ru'],
        }),
        ('Түрү жана файл', {
            'fields': ['type', 'image', 'file'],
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