from rest_framework import serializers
from apps.administration.models import Report, ReportImage, TitleAdministration, TypeAdministration, Management, Structure, Vacancy, AntiCorruptionMeasures


class TypeAdministrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeAdministration
        fields = ('id', 'type')


class TitleAdministrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TitleAdministration
        fields = ["id", "title"]


class ManagementSerializer(serializers.ModelSerializer):
    type = TypeAdministrationSerializer(read_only=True)
    
    class Meta:
        model = Management
        fields = ('id', 'type', 'role', 'full_name', 'reseptions', 'image')


class StructureSerializer(serializers.ModelSerializer):
    type = TypeAdministrationSerializer(read_only=True)

    class Meta:
        model = Structure
        fields = ('id', 'type', 'image')


class VacancySerializer(serializers.ModelSerializer):
    type = TypeAdministrationSerializer(read_only=True)

    class Meta:
        model = Vacancy
        fields = ('id', 'type', 'title', 'description')


class AntiCorruptionMeasuresItemSerializer(serializers.ModelSerializer):
    common_title = TitleAdministrationSerializer(read_only=True)
    file = serializers.SerializerMethodField()

    class Meta:
        model = AntiCorruptionMeasures
        fields = (
            'common_title',
            'title',
            'real_title',
            'description',
            'real_description',
            'image',
            'file',
        )

    def get_file(self, obj):
        return obj.file.url if obj.file else None


class AntiCorruptionMeasuresSerializer(serializers.ModelSerializer):
    type = TypeAdministrationSerializer(read_only=True)
    items = serializers.SerializerMethodField()

    class Meta:
        model = AntiCorruptionMeasures
        fields = ('id', 'type', 'items')

    def get_items(self, obj):
        return [
            AntiCorruptionMeasuresItemSerializer(
                obj,
                context=self.context
            ).data
        ]


class ReportImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportImage
        fields = ['id', 'image']


class ReportSerializer(serializers.ModelSerializer):
    type = TypeAdministrationSerializer(read_only=True)
    common_title = TitleAdministrationSerializer(read_only=True)
    images = ReportImageSerializer(many=True, read_only=True)

    class Meta:
        model = Report
        fields = [
            'id', 'type', 'common_title', 'title', 'description', 'images'
        ]