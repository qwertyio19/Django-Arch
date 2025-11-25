from rest_framework.routers import DefaultRouter
from apps.base.views import CartViewSet, HeadlinesViewSet, FooterViewSet, VisitorStatisticsViewSet

router = DefaultRouter()
router.register(r'cart', CartViewSet)
router.register(r'headlines', HeadlinesViewSet)

router.register(r'footer', FooterViewSet, basename='footer')
router.register(r'statistics', VisitorStatisticsViewSet, basename='statistics')

urlpatterns = router.urls
