from rest_framework import mixins, viewsets
from .models import TypeNotification, Notification
from .serializers import TypeNotificationSerializer, NotificationSerializer


class TypeNotificationView(mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    queryset = TypeNotification.objects.all()
    serializer_class = TypeNotificationSerializer


class NotificationView(mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
