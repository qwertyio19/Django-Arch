from rest_framework.routers import DefaultRouter
from apps.district.views import TypeTitleViewSet, DataViewSet

router = DefaultRouter()

router.register(r'type', TypeTitleViewSet, basename='type_district')
router.register(r'data', DataViewSet, basename='data_district')


urlpatterns = router.urls