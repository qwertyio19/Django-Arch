from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('cart', CartViewSet)
router.register('headlines', HeadlinesViewSet)

urlpatterns = router.urls
