from rest_framework.routers import DefaultRouter
from apps.base.views import CartViewSet, HeadlinesViewSet, FooterViewSet, VisitorStatisticsViewSet, PagetitlesViewSets

router = DefaultRouter()
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'headlines', HeadlinesViewSet, basename='headlines')

router.register(r'footer', FooterViewSet, basename='footer')
router.register(r'statistics', VisitorStatisticsViewSet, basename='statistics')

router.register(r'pagetitles', PagetitlesViewSets, basename='pagetitles')

urlpatterns = router.urls
