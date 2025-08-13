from django.db import models
from django.contrib.auth.models import User
from .inquiries import Inquiry
from .staff import Staff

class Booking(models.Model):
    STATUS_CHOICES = [
        ('CONFIRMED', 'Confirmed'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]
    
    inquiry = models.OneToOneField(Inquiry, on_delete=models.CASCADE)
    booking_staff = models.ManyToManyField(Staff, through='BookingStaff')
    booking_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='CONFIRMED')
    total_estimated_cost = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)