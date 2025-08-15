from rest_framework import serializers
from audioapi.models import Booking
from .BookingStaffSerializer import BookingStaffSerializer

class BookingSerializer(serializers.ModelSerializer):
    booking_staff_assignments = BookingStaffSerializer(
        source='bookingstaff_set', many=True, read_only=True
    )
    inquiry_title = serializers.CharField(source='inquiry.title', read_only=True)
    
    class Meta:
        model = Booking
        fields = [
            'id', 'inquiry', 'inquiry_title', 'booking_date', 'end_date', 
            'status', 'total_estimated_cost', 'notes', 'created_at',
            'booking_staff_assignments'
        ]