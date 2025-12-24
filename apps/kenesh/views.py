from rest_framework import mixins, viewsets
from .models import CouncilSection, CouncilDocument, Deputies, Commission
from .serializers import CouncilSectionSerializer, CouncilDocumentSerializer, DeputiesSerializer, CommissionSerializer


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


class DeputiesViewSet(mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    queryset = Deputies.objects.all()
    serializer_class = DeputiesSerializer


class CommissionViewSet(mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    queryset = Commission.objects.all()
    serializer_class = CommissionSerializer