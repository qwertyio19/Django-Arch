from modeltranslation.translator import register, TranslationOptions
from apps.news.models import News


@register(News)
class NewsTranslation(TranslationOptions):
    fields = (
        'name', 'description', 'date'
    )