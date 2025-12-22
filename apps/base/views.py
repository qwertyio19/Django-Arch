from apps.base.models import *
from apps.base.seriallizers import *
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.response import Response as response

class CartViewSet(viewsets.ModelViewSet):
    queryset = CartModel.objects.all()
    serializer_class = CartSerializer

class HeadlinesViewSet(viewsets.ModelViewSet):
    queryset = HeadlinesModel.objects.all()
    serializer_class = HeadlinesSerializer

class FooterViewSet(mixins.RetrieveModelMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer
    permission_classes = [AllowAny]

class VisitorStatisticsViewSet(viewsets.ViewSet):
    def list(self, request):
        data = VisitorStatistics.get_total_statistics()
        return response(data)
    
class PagetitlesViewSets(viewsets.ModelViewSet):
    queryset = PagetitlesModel.objects.all()
    serializer_class = PagetitlesSeriallizers


class DataViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Portal.objects.all()
    serializer_class = PortalSerializer


class LatestNewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LatestNews.objects.all()
    serializer_class = LatestNewsSerializer
