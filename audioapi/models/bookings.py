from django.db import models
from django.contrib.auth.models import User
from .inquiries import Inquiry

class Booking(models.Model):
    inquiry_id = models.ForeignKey(Inquiry, on_delete=models.CASCADE, related_name='inquiryid')
    event_date = models.DateField(null=True)
    confirmed_by_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='confirmedbyuser')
    confirmed_at = models.DateField(auto_now_add=True)