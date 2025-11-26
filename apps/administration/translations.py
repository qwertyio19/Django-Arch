from modeltranslation.translator import register, TranslationOptions
from apps.administration.models import TypeAdministration, Management


@register(TypeAdministration)
class TypeAdministrationTranslation(TranslationOptions):
    fields = ('type',)

@register(Management)
class ManagementTranslation(TranslationOptions):
    fields = ('role', 'full_name', 'reseptions')