from django.urls import path
from apps.notifications.views import AnnouncementListMixinView, TitleListMixinView, AnnouncementByTitleMixinView

urlpatterns = [
    path('titles/', TitleListMixinView.as_view(), name='titles-list'),
    path('announcements/', AnnouncementListMixinView.as_view(), name='announcements-list'),
    path('titles/<int:title_id>/announcements/', AnnouncementByTitleMixinView.as_view(), name='announcements-by-title'),

]
