from modeltranslation.translator import register, TranslationOptions
from apps.administration.models import Report, TypeAdministration, Management, Vacancy, AntiCorruptionMeasures, TitleAdministration


@register(TypeAdministration)
class TypeAdministrationTranslation(TranslationOptions):
    fields = ('type',)

@register(TitleAdministration)
class TitleAdministrationTranslation(TranslationOptions):
    fields = ('title',)

@register(Management)
class ManagementTranslation(TranslationOptions):
    fields = ('role', 'full_name', 'reseptions')

@register(Vacancy)
class VacancyTranslation(TranslationOptions):
    fields = ('title', 'description')

@register(AntiCorruptionMeasures)
class AntiCorruptionMeasuresTranslation(TranslationOptions):
    fields = ('title', 'real_title', 'description', 'real_description')

@register(Report)
class ReportTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)