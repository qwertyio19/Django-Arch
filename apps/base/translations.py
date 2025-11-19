from modeltranslation.translator import register, TranslationOptions
from apps.base.models import *

@register(CartModel)
class CatalogsTranslation(TranslationOptions):
    fields = ('title', 'description')


@register(HeadlinesModel)
class HeadlinesTranslation(TranslationOptions):
    fields = ('KokBelLocalGovernment', 'Announcements', 'Latestannouncements', 'Anticorruptionmeasures', 'Governmentportal', 'Jobs')
