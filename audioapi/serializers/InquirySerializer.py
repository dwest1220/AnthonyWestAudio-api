from rest_framework import serializers
from audioapi.models import Inquiry
import datetime

class InquirySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Inquiry
        fields = ['id', 'status', 'user', 'event_name', 'event_date', 'location', 'message', 'created_at']
    
    def validate_event_date(self, value):
        if value and value < datetime.date.today():
            raise serializers.ValidationError("Event date cannot be in the past.")
        return value
        