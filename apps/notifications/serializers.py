from rest_framework import serializers
from apps.notifications.models import TypeNotification, Notification


class TypeNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeNotification
        fields = ["id", "type"]


class NotificationSerializer(serializers.ModelSerializer):
    types = TypeNotificationSerializer(read_only=True)

    class Meta:
        model = Notification
        fields = [
            "id",
            "types",
            "title",
            "description",
            'date',
            "image",
        ]