from rest_framework import serializers
from audioapi.models import Staff
from .UserSerializer import UserSerializer

class StaffSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    full_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Staff
        fields = ['id', 'user', 'role', 'day_rate', 'is_active', 'bio', 'created_at', 'full_name']
    
    def get_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}".strip() or obj.user.username