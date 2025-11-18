from apps.notifications.admin import *
from apps.notifications.models import *
from modeltranslation.translator import translator, TranslationOptions

class TitleTranslationOptions(TranslationOptions):
    fields = ('name',)

class AnnouncementTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'link')



# Регистрация переводов
translator.register(Title, TitleTranslationOptions)
translator.register(Announcement, AnnouncementTranslationOptions)
