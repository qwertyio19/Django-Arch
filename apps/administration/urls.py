from rest_framework.routers import DefaultRouter
from apps.administration.views import TypeAdministrationViewSet, ManagementViewSet

router = DefaultRouter()

router.register(r'type', TypeAdministrationViewSet, basename='type-administration')
router.register(r'management', ManagementViewSet, basename='management')


urlpatterns = router.urls