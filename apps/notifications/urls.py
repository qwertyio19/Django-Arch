from django.urls import path
from apps.notifications.views import AnnouncementViewSet, TitleViewSet

urlpatterns = [
    path('titles/', TitleViewSet.as_view({'get': 'list'}), name='titles-list'),
    path('titles/<int:pk>/', TitleViewSet.as_view({'get': 'retrieve'}), name='title-detail'),
    path('announcements/', AnnouncementViewSet.as_view({'get': 'list'}), name='announcements-list'),
    path('announcements/<int:pk>/', AnnouncementViewSet.as_view({'get': 'retrieve'}), name='announcement-detail'),

]
