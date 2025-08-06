from django.db import models
from .bookings import Booking
from .staff import Staff 

class BookingStaff(models.Model):
    booking = models.ForeignKey(
        Booking,
        on_delete=models.CASCADE,
        related_name='bookingstaff'
    )
    
    staff = models.ForeignKey(
        Staff,
        on_delete=models.CASCADE,
        related_name='staffbooking'
    )