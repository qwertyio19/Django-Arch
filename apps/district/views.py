from rest_framework import viewsets
from apps.district.models import TypeTitle, Data
from apps.district.serializers import TypeTitleSerializer, DataSerializer


class TypeTitleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TypeTitle.objects.all()
    serializer_class = TypeTitleSerializer


class DataViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer