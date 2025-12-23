from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from apps.base.translations import *
from apps.base.models import CartModel, Visit, VisitorStatistics


class CartAdmin(TranslationAdmin):
    fieldsets = (
        ('Кыргызская версия', {
            'fields': ['head_ky', 'full_name_ky', 'words_ky', 'description_ky'],
        }),
        ('Русская версия', {
            'fields': ['head_ru', 'full_name_ru', 'words_ru', 'description_ru'],
        }),
        ('Изображния', {
            'fields': ['image'],
        }),
    )
admin.site.register(CartModel, CartAdmin)




class HeadlinesAdmin(TranslationAdmin):
    fieldsets = (
        ('Кыргызская версия', {
            'fields': ['KokBelLocalGovernment_ky', 'Announcements_ky', 'Latestannouncements_ky', 'Anticorruptionmeasures_ky', 'Governmentportal_ky', 'Jobs_ky'],
        }),
        ('Русская версия', {
            'fields': ['KokBelLocalGovernment_ru', 'Announcements_ru', 'Latestannouncements_ru', 'Anticorruptionmeasures_ru', 'Governmentportal_ru', 'Jobs_ru'],
        }),
    )
admin.site.register(HeadlinesModel, HeadlinesAdmin)



@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if Footer.objects.exists():
            return False
        return True
    
    fieldsets = (
        ('Кыргызский язык', {
            'fields': (
                'address_ky', 'home_ky', 'aiyl_aimagy_ky', 'aiyl_okmotu_ky', 
                'aiyldyk_kenesh_ky', 'obrashenie_gragdan_ky', 'novosti_ky', 
                'obiavlenie_ky','soicial_media_ky'
            )
        }),
        ('Русский язык', {
            'fields': (
                'address_ru', 'home_ru', 'aiyl_aimagy_ru', 'aiyl_okmotu_ru', 
                'aiyldyk_kenesh_ru', 'obrashenie_gragdan_ru', 'novosti_ru', 
                'obiavlenie_ru','soicial_media_ru'
            )
        }),
        ('Основное', {
            'fields': (
                'logo', 'navigation','title_phone', 'phone','title_address', 
                'facebook', 'statistic_title'
            )
        }),
    )


@admin.action(description='Reset visitors count to zero')
def reset_visitors(modeladmin, request, queryset):
    queryset.update(visitors=0)

class VisitorStatisticsAdmin(admin.ModelAdmin):
    
    def has_add_permission(self, request):
        if Footer.objects.exists():
            return False
        return True
    
    list_display = ['date', 'visitors']
    actions = [reset_visitors]
admin.site.register(VisitorStatistics, VisitorStatisticsAdmin)

class PagetitlesAdmin(TranslationAdmin):
    fieldsets = (
        ('Кыргызская версия', {
            'fields': ['ruraldistrict_ky', 'ruralcouncil_ky', 'villagecouncil_ky', 'news_ky', 'announcement_ky'],
        }),
        ('Русская версия', {
            'fields': ['ruraldistrict_ru', 'ruralcouncil_ru', 'villagecouncil_ru', 'news_ru', 'announcement_ru'],
        }),
    )
admin.site.register(PagetitlesModel, PagetitlesAdmin)


class PortalAdmin(TranslationAdmin):
    fieldsets = (
        ('Кыргызская версия', {
            'fields': ['title_ky'],
        }),
        ('Русская версия', {
            'fields': ['title_ru'],
        }),
        ('Фото жана шилтеме', {
            'fields': ['image', 'link'],
        }),
    )
admin.site.register(Portal, PortalAdmin)


class LatestNewsAdmin(TranslationAdmin):
    fieldsets = (
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky'],
        }),
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru'],
        }),
        ('Изображния', {
            'fields': ['image'],
        }),
    )
admin.site.register(LatestNews, LatestNewsAdmin)


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ("ip_address", "path", "timestamp")
    actions = ["clear_statistics"]

    def clear_statistics(self, request, queryset):
        """
        Очистка всех записей статистики.
        """
        Visit.objects.all().delete()
        self.message_user(request, "Все записи статистики удалены.")
    clear_statistics.short_description = "Очистить всю статистику"