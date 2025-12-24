from rest_framework import viewsets
from apps.administration.models import Report, TitleAdministration, TypeAdministration, Management, Structure, Vacancy, AntiCorruptionMeasures
from apps.administration.serializers import ReportSerializer, TitleAdministrationSerializer, TypeAdministrationSerializer, ManagementSerializer, StructureSerializer, VacancySerializer, AntiCorruptionMeasuresSerializer

class TypeAdministrationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TypeAdministration.objects.all()
    serializer_class = TypeAdministrationSerializer


class ManagementViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Management.objects.all()
    serializer_class = ManagementSerializer


class StructureViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Structure.objects.all()
    serializer_class = StructureSerializer


class VacancyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


class AntiCorruptionMeasuresViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AntiCorruptionMeasures.objects.all()
    serializer_class = AntiCorruptionMeasuresSerializer


class ReportViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class TitleAdministrationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TitleAdministration.objects.all()
    serializer_class = TitleAdministrationSerializer