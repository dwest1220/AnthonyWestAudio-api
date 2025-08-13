from django.db import models
from django.contrib.auth.models import User

class Staff(models.Model):
    ROLE_CHOICES = [
        ('FOH_ENGINEER', 'FOH Engineer'),
        ('MONITOR_ENGINEER', 'Monitor Engineer'),
        ('PRODUCTION_MANAGER', 'Production Manager'),
        ('VIDEO_ENGINEER', 'Video Engineer'),
        ('LIGHTING_TECH', 'Lighting Technician'),
        ('AUDIO_TECH', 'Audio Technician'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    day_rate = models.DecimalField(max_digits=6, decimal_places=2)
    is_active = models.BooleanField(default=True)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    