from django.db import models
from django.contrib.auth.models import User

class Inquiry(models.Model):
    class Status(models.TextChoices):
        TENTATIVE = 'TENTATIVE', 'Tentative'
        SIGNING = 'SIGNING', 'Signing'
        DEFINITE = 'DEFINITE', 'Definite'
        CANCELLED = 'CANCELLED', 'Cancelled'

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.TENTATIVE
        )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inquiries')
    event_name = models.CharField(max_length=100)
    event_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=70)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)