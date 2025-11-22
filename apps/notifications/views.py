from rest_framework import mixins, viewsets
from .models import Title, Description
from .serializers import TitleSerializer, DescriptionSerializer


class TitleViewSet(mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


class DescriptionViewSet(mixins.ListModelMixin,
                             mixins.RetrieveModelMixin,
                             viewsets.GenericViewSet):
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        section_id = self.request.query_params.get("section")
        if section_id:
            qs = qs.filter(section_id=section_id)
        return qs