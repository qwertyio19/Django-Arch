from django.utils.translation import gettext_lazy as _  
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from apps.notifications.models import Announcement, Title
from apps.notifications.serializers import AnnouncementSerializer, TitleSerializer

class AnnouncementViewSet(GenericViewSet,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         ):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

class TitleViewSet(GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    ):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer