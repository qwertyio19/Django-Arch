from rest_framework.routers import DefaultRouter
from apps.notifications.views import TitleViewSet, DescriptionViewSet


router = DefaultRouter()
router.register(r"titles", TitleViewSet, basename="title")
router.register(r"descriptions", DescriptionViewSet, basename="description")


urlpatterns = router.urls