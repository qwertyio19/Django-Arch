from rest_framework import viewsets
from apps.administration.models import TypeAdministration, Management
from apps.administration.serializers import TypeAdministrationSerializer, ManagementSerializer

class TypeAdministrationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TypeAdministration.objects.all()
    serializer_class = TypeAdministrationSerializer


class ManagementViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Management.objects.all()
    serializer_class = ManagementSerializer