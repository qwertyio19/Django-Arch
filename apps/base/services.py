from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.base.models import Visit


@api_view(["GET"])
def stats_summary(request):
    total_views = Visit.objects.count()
    
    unique_visitors = Visit.objects.values("ip_address").distinct().count()

    return Response({
        "total_views": total_views,
        "unique_visitors": unique_visitors
    })
