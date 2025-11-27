from rest_framework.routers import DefaultRouter
from apps.administration.views import ReportViewSet, TitleAdministrationViewSet, TypeAdministrationViewSet, ManagementViewSet, StructureViewSet, VacancyViewSet, AntiCorruptionMeasuresViewSet

router = DefaultRouter()

router.register(r'type', TypeAdministrationViewSet, basename='type-administration')
router.register(r'management', ManagementViewSet, basename='management')
router.register(r'structure', StructureViewSet, basename='structure')
router.register(r'vacancy', VacancyViewSet, basename='vacancy')
router.register(r'anti', AntiCorruptionMeasuresViewSet, basename='anti')
router.register(r'reports', ReportViewSet, basename='report')
router.register(r"common_title", TitleAdministrationViewSet, basename="common_title")


urlpatterns = router.urls