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


class AntiCorruptionMeasuresSerializer(serializers.ModelSerializer):
    type = TypeAdministrationSerializer(read_only=True)
    common_title = TitleAdministrationSerializer(read_only=True)
    class Meta:
        model = AntiCorruptionMeasures
        fields = ('id', 'type', 'common_title', 'title', 'real_title', 'description', 'real_description', 'file', 'content_html')


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