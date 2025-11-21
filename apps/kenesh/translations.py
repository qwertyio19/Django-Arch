# app/council/translation.py
from modeltranslation.translator import register, TranslationOptions
from .models import CouncilSection, CouncilDocument


@register(CouncilSection)
class CouncilSectionTranslation(TranslationOptions):
    fields = ("title", "detail_title")


@register(CouncilDocument)
class CouncilDocumentTranslation(TranslationOptions):
    fields = ("title", "description", "content_html")
