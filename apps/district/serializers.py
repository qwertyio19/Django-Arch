from rest_framework import serializers
from apps.district.models import TypeTitle, Data, DataImage


class TypeTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeTitle
        fields = ('id', 'type', 'title')


class DataImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataImage
        fields = ['id', 'image']


class DataSerializer(serializers.ModelSerializer):
    type_title = TypeTitleSerializer(read_only=True)
    images = DataImageSerializer(many=True, read_only=True)
    year = serializers.SerializerMethodField()

    class Meta:
        model = Data
        fields = ('id', 'type_title', 'year', 'description', 'images')

    def get_year(self, obj):
        return obj.date.year if obj.date else None