from modeltranslation.translator import register, TranslationOptions
from apps.base.models import CartModel, HeadlinesModel, Footer, PagetitlesModel, Portal

@register(CartModel)
class CatalogsTranslation(TranslationOptions):
    fields = ('title', 'description')


@register(HeadlinesModel)
class HeadlinesTranslation(TranslationOptions):
    fields = ('KokBelLocalGovernment', 'Announcements', 'Latestannouncements', 'Anticorruptionmeasures', 'Governmentportal', 'Jobs')


@register(Footer)
class FooterTranslation(TranslationOptions):
    fields = (
        'home', 'address', 'aiyl_aimagy', 'aiyl_okmotu', 'aiyldyk_kenesh',
        'obrashenie_gragdan', 'novosti', 'obiavlenie', 'soicial_media'
    )
@register(PagetitlesModel)
class PagetitlesTranslation(TranslationOptions):
    fields = ('ruraldistrict', 'ruralcouncil', 'villagecouncil', 'news', 'announcement')


@register(Portal)
class PortalTranslation(TranslationOptions):
    fields = ('title',)