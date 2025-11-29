from modeltranslation.translator import register, TranslationOptions
from apps.district.models import TypeTitle, Data, DataImage


@register(TypeTitle)
class TypeTitleTranslation(TranslationOptions):
    fields = ('type', 'title')

@register(Data)
class DataTranslation(TranslationOptions):
    fields = ('date', 'description')