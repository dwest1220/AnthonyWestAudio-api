from django.db import models
from .booking import Booking
from .staff import Staff 

class BookingStaff(models.Model):
    RATE_TYPE_CHOICES = [
        ('FULL_DAY', 'Full Day'),
        ('HALF_DAY', 'Half Day'),
        ('CUSTOM', 'Custom Rate'),
    ]
    
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    rate_type = models.CharField(max_length=20, choices=RATE_TYPE_CHOICES, default='FULL_DAY')
    day_rate_at_booking = models.DecimalField(max_digits=6, decimal_places=2)
    custom_rate = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    days_worked = models.PositiveIntegerField(default=1)
    notes = models.TextField(blank=True)
    assigned_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_cost(self):
        if self.rate_type == 'CUSTOM' and self.custom_rate:
            return self.custom_rate * self.days_worked
        return self.day_rate_at_booking * self.days_worked