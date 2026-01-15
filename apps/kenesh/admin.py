from django.contrib import admin
from django.core.exceptions import ValidationError
from django import forms
from modeltranslation.admin import TranslationAdmin
from .models import CouncilSection, CouncilDocument, Deputies, Commission
from .translations import *


def validate_pdf(f):
    name = (f.name or "").lower()
    if not name.endswith(".pdf"):
        raise ValidationError("Разрешены только PDF файлы (.pdf).")

    # опционально (если файл пришел через upload и есть content_type)
    content_type = getattr(f, "content_type", None)
    if content_type and content_type != "application/pdf":
        raise ValidationError("Файл должен быть PDF (application/pdf).")


class CouncilDocumentAdminForm(forms.ModelForm):
    def clean_file(self):
        f = self.cleaned_data.get("file")
        if f:
            validate_pdf(f)
        return f

    class Meta:
        model = CouncilDocument
        fields = "__all__"


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
    form = CouncilDocumentAdminForm
    fieldsets = (
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky'],
        }),
        ('Файл', {
            'fields': ['section', 'file'],
        }),
    )

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
            'fields': ['section', 'real_contact', 'image', 'is_first'],
        }),
    )

    list_display = ['name_ky', 'position_ky', 'section', 'is_first']
    list_filter = ['section']
    search_fields = ['name_ru', 'name_ky', 'position_ru', 'position_ky']

    def save_model(self, request, obj, form, change):
        if obj.is_first:
            if Deputies.objects.filter(is_first=True).exclude(id=obj.id).exists():
                form.add_error('is_first', "Только один депутат может быть первым.")
                return

        super().save_model(request, obj, form, change)

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