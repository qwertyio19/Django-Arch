from rest_framework import serializers
from .models import Title, Description


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ["id", "title"]


class DescriptionSerializer(serializers.ModelSerializer):
    section = TitleSerializer(read_only=True)

    class Meta:
        model = Description
        fields = [
            "id",
            "section",
            "title",
            "description",
            "content_html",
        ]