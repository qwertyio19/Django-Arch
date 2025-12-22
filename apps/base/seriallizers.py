from rest_framework import serializers
from rest_framework import serializers
from apps.base.models import Footer, LatestNews, VisitorStatistics, HeadlinesModel, CartModel, PagetitlesModel, Portal

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartModel
        fields = ['id', 'head', 'full_name', 'words', 'description', 'image']

class HeadlinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeadlinesModel
        fields = ['id', 'KokBelLocalGovernment', 'Announcements', 'Latestannouncements', 'Anticorruptionmeasures', 'Governmentportal', 'Jobs']


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = [
            'logo', 'navigation','home','aiyl_aimagy', 
            'aiyl_okmotu', 'aiyldyk_kenesh', 'obrashenie_gragdan', 
            'novosti','obiavlenie', 'soicial_media', 'address', 
            'title_address', 'title_phone', 'phone', 'facebook', 'statistic_title'
        ]

class VisitorStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorStatistics
        fields = ["date", "visitors"]


class PagetitlesSeriallizers(serializers.ModelSerializer):
    class Meta:
        model = PagetitlesModel
        fields = ['id', 'ruraldistrict', 'ruralcouncil', 'villagecouncil', 'news', 'announcement']
        


class PortalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portal
        fields = ['id', 'title', 'image', 'link']



class LatestNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LatestNews
        fields = ['id', 'title', 'image', 'description']
