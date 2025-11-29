from rest_framework.routers import DefaultRouter
from apps.kenesh.views import CouncilSectionViewSet, CouncilDocumentViewSet, DeputiesViewSet, CommissionViewSet


router = DefaultRouter()
router.register(r"council-sections", CouncilSectionViewSet, basename="council-section")
router.register(r"council-documents", CouncilDocumentViewSet, basename="council-document")
router.register(r"deputies", DeputiesViewSet, basename="deputies")
router.register(r"commissions", CommissionViewSet, basename="commission")


urlpatterns = router.urls
