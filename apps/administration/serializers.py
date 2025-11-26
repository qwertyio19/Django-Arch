from rest_framework import serializers
from apps.administration.models import TypeAdministration, Management


class TypeAdministrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeAdministration
        fields = ('id', 'type')


class ManagementSerializer(serializers.ModelSerializer):
    type = TypeAdministrationSerializer(read_only=True)
    
    class Meta:
        model = Management
        fields = ('id', 'type', 'role', 'full_name', 'reseptions', 'image')