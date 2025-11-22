from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.notifications.views import AnnouncementViewSet, TitleViewSet

router = DefaultRouter()
router.register(r'announcements', AnnouncementViewSet, basename='announcement')
router.register(r'titles', TitleViewSet, basename='title')

urlpatterns = [
    path('notifications/', include(router.urls)),
]