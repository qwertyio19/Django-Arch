from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from apps.base.translations import *
from apps.base.models import CartModel, VisitorStatistics


class CartAdmin(TranslationAdmin):
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

class PagetitlesAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Кыргызская версия', {
            'fields': ['ruraldistrict_ky', 'ruralcouncil_ky', 'vilagecouncil_ky', 'news_ky', 'announcement_ky'],
        }),
        ('Русская версия', {
            'fields': ['ruraldistrict_ru', 'ruralcouncil_ru', 'vilagecouncil_ru', 'news_ru', 'announcement_ru'],
        }),
    )