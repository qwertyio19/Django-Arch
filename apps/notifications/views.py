from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
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
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['types']

    @action(detail=False, methods=['get'], url_path='active')
    def active_notifications(self, request):
        active_notifications = Notification.objects.filter(is_active=True)
        page = self.paginate_queryset(active_notifications)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(active_notifications, many=True)
        return Response(serializer.data)