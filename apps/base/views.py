from apps.base.models import *
from apps.base.seriallizers import *
from rest_framework import viewsets


class CartViewSet(viewsets.ModelViewSet):
    queryset = CartModel.objects.all()
    serializer_class = CartSerializer

class HeadlinesViewSet(viewsets.ModelViewSet):
    queryset = HeadlinesModel.objects.all()
    serializer_class = HeadlinesSerializer