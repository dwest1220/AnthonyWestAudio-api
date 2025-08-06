from rest_framework import serializers
from audioapi.models import Inquiry

class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = ['id', 'status', 'event_name', 'event_date', 'location', 'message', 'created_at']