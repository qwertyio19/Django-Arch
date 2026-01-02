from rest_framework import serializers
from .models import CouncilSection, CouncilDocument, Deputies, Commission


class CouncilSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CouncilSection
        fields = ["id", "title", "detail_title"]


class CouncilDocumentSerializer(serializers.ModelSerializer):
    section = CouncilSectionSerializer(read_only=True)
    file = serializers.SerializerMethodField()

    class Meta:
        model = CouncilDocument
        fields = [
            "id",
            "section",
            "title",
            "description",
            "file",
        ]

    def get_file(self, obj):
        return obj.file.url if obj.file else None


class DeputiesSerializer(serializers.ModelSerializer):
    section = CouncilSectionSerializer(read_only=True)
    class Meta:
        model = Deputies
        fields = ["id", 'section', 'position', 'name', 'contact', 'real_contact', 'district', 'real_district', 'faction', 'real_faction', 'role', 'real_role', 'image', 'is_first']


class CommissionSerializer(serializers.ModelSerializer):
    section = CouncilSectionSerializer(read_only=True)

    class Meta:
        model = Commission
        fields = ["id", 'section', 'position', 'name', 'contact', 'real_contact', 'district', 'real_district', 'faction', 'real_faction', 'role', 'real_role', 'image']