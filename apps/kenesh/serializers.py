# app/council/serializers.py
from rest_framework import serializers
from .models import CouncilSection, CouncilDocument


class CouncilSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CouncilSection
        fields = ["id", "title", "detail_title"]  # modeltranslation подставит активный язык


class CouncilDocumentSerializer(serializers.ModelSerializer):
    section = CouncilSectionSerializer(read_only=True)

    class Meta:
        model = CouncilDocument
        # file тут НЕ отдаем — только текст для сайта
        fields = [
            "id",
            "section",
            "title",
            "description",
            "content_html",
        ]
