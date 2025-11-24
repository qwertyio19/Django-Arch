from modeltranslation.translator import register, TranslationOptions
from .models import Title, Description


@register(Title)
class TitleTranslation(TranslationOptions):
    fields = ("title",)


@register(Description)
class DescriptionTranslation(TranslationOptions):
    fields = ("title", "description")