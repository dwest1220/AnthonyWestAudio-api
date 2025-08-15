from rest_framework import serializers
from audioapi.models import BookingStaff, Staff
from .StaffSerializer import StaffSerializer

class BookingStaffSerializer(serializers.ModelSerializer):
    staff = StaffSerializer(read_only=True)
    staff_id = serializers.IntegerField(write_only=True)
    total_cost = serializers.ReadOnlyField()
    
    class Meta:
        model = BookingStaff
        fields = [
            'id', 'booking', 'staff', 'staff_id', 'rate_type', 
            'day_rate_at_booking', 'custom_rate', 'days_worked', 
            'notes', 'assigned_at', 'total_cost'
        ]
    
    def create(self, validated_data):
        staff_id = validated_data.pop('staff_id')
        staff = Staff.objects.get(id=staff_id)
        
        # Auto-populate day_rate_at_booking from staff's current rate
        if 'day_rate_at_booking' not in validated_data:
            validated_data['day_rate_at_booking'] = staff.day_rate
            
        validated_data['staff'] = staff
        return super().create(validated_data)