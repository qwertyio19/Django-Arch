from rest_framework import serializers
from .models import CartModel, HeadlinesModel

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartModel
        fields = ['id', 'title', 'description', 'image']

class HeadlinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeadlinesModel
        fields = ['id', 'KokBelLocalGovernment', 'Announcements', 'Latestannouncements', 'Anticorruptionmeasures', 'Governmentportal', 'Jobs']