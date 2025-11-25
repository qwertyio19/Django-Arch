from modeltranslation.translator import register, TranslationOptions
from .models import TypeNotification, Notification


@register(TypeNotification)
class TypeNotificationTranslation(TranslationOptions):
    fields = ("type",)

@register(Notification)
class NotificationTranslation(TranslationOptions):
    fields = ('types', "title", "description")