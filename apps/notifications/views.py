from rest_framework import mixins, viewsets
from apps.notifications.models import TypeNotification, Notification
from apps.notifications.serializers import TypeNotificationSerializer, NotificationSerializer
from apps.notifications.paginations import NotificationPagination


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
    pagination_class = NotificationPagination
