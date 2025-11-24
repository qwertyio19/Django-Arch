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
