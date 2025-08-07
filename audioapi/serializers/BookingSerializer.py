from rest_framework import serializers
from audioapi.models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'event_date','confirmed_by_user', 'confirmed_at']