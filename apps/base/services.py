# statistics/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.base.models import Visitor, PageVisit


class SiteStatisticsView(APIView):
    def get(self, request, *args, **kwargs):
        
        unique_visitors_count = Visitor.objects.count()

        total_views_count = PageVisit.objects.count()

        return Response({
            "total_views": total_views_count,
            "unique_visitors": unique_visitors_count
        })