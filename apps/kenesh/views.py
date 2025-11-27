# app/council/views.py
from rest_framework import mixins, viewsets
from .models import CouncilSection, CouncilDocument
from .serializers import CouncilSectionSerializer, CouncilDocumentSerializer


class CouncilSectionViewSet(mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    queryset = CouncilSection.objects.all()
    serializer_class = CouncilSectionSerializer


class CouncilDocumentViewSet(mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    queryset = CouncilDocument.objects.all()
    serializer_class = CouncilDocumentSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        section_id = self.request.query_params.get("section")
        if section_id:
            qs = qs.filter(section_id=section_id)
        return qs
