from rest_framework import viewsets
from apps.news.models import News
from apps.news.serializers import NewsSerializer
from apps.news.paginations import NewsPagination

class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = NewsPagination