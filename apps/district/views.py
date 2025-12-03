from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from apps.district.models import TypeTitle, Data
from apps.district.serializers import TypeTitleSerializer, DataSerializer


class TypeTitleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TypeTitle.objects.all()
    serializer_class = TypeTitleSerializer


class DataViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DataSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['date']
    ordering = ['-date']

    def get_queryset(self):
        queryset = (
            Data.objects
            .all()
            .select_related('type_title')
            .prefetch_related('images')
        )

        year = self.request.query_params.get('year')
        type_id = self.request.query_params.get('type_title') or self.request.query_params.get('type')

        if year:
            queryset = queryset.filter(date__year=year)

        if type_id:
            queryset = queryset.filter(type_title_id=type_id)

        return queryset
