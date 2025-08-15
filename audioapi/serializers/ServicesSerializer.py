from rest_framework import serializers
from audioapi.models import Staff

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['id', 'name', 'description', 'price']