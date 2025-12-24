from modeltranslation.translator import register, TranslationOptions
from .models import CouncilSection, CouncilDocument, Deputies, Commission


@register(CouncilSection)
class CouncilSectionTranslation(TranslationOptions):
    fields = ("title", "detail_title")


@register(CouncilDocument)
class CouncilDocumentTranslation(TranslationOptions):
    fields = ("title", "description")


@register(Deputies)
class DeputiesTranslation(TranslationOptions):
    fields = ('position', 'name', 'contact', 'district', 'real_district', 'faction', 'real_faction', 'role', 'real_role')


@register(Commission)
class CommissionTranslation(TranslationOptions):
    fields = ('position', 'name', 'contact', 'district', 'real_district', 'faction', 'real_faction', 'role', 'real_role')
