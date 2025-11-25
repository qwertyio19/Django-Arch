from rest_framework.routers import DefaultRouter
from apps.kenesh.views import CouncilSectionViewSet, CouncilDocumentViewSet


router = DefaultRouter()
router.register(r"council-sections", CouncilSectionViewSet, basename="council-section")
router.register(r"council-documents", CouncilDocumentViewSet, basename="council-document")


urlpatterns = router.urls
