from rest_framework import serializers
from .models import CouncilSection, CouncilDocument


class CouncilSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CouncilSection
        fields = ["id", "title", "detail_title"]


class CouncilDocumentSerializer(serializers.ModelSerializer):
    section = CouncilSectionSerializer(read_only=True)

    class Meta:
        model = CouncilDocument
        fields = [
            "id",
            "section",
            "title",
            "description",
            "content_html",
        ]
