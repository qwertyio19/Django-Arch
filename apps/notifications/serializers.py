from rest_framework import serializers
from apps.notifications.models import Title, Announcement

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['id', 'image', 'description', 'link']

class TitleSerializer(serializers.ModelSerializer):
    announcements = AnnouncementSerializer(many=True, read_only=True)
    class Meta:
        model = Title
        fields = ['id', 'name', 'announcements']
