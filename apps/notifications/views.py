from rest_framework import mixins, generics, viewsets
from apps.notifications.models import Title, Announcement
from apps.notifications.serializers import TitleSerializer, AnnouncementSerializer


class TitleListMixinView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class AnnouncementListMixinView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class AnnouncementByTitleMixinView(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = AnnouncementSerializer

    def get_queryset(self):
        title_id = self.kwargs['title_id']
        return Announcement.objects.filter(title_id=title_id)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
