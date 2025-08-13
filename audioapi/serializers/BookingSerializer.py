from rest_framework import serializers
from audioapi.models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'status', 'booking_staff', 'booking_date', 'end_date', 'status', 'total_estimated_cost', 'notes', 'created_at']