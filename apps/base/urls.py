from rest_framework.routers import DefaultRouter
from apps.base.views import CartViewSet, DataViewSet, HeadlinesViewSet, FooterViewSet, LatestNewsViewSet, VisitorStatisticsViewSet, PagetitlesViewSets

router = DefaultRouter()
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'headlines', HeadlinesViewSet, basename='headlines')

router.register(r'footer', FooterViewSet, basename='footer')
router.register(r'statistics', VisitorStatisticsViewSet, basename='statistics')

router.register(r'pagetitles', PagetitlesViewSets, basename='pagetitles')
router.register(r'portal', DataViewSet, basename='portal')

router.register(r'latest_news', LatestNewsViewSet, basename='latest_news')


urlpatterns = router.urls
