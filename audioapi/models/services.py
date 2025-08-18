from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    details = models.TextField(blank=True)
    icon = models.TextField()
    price = models.FloatField(
        validators=[MinValueValidator(0.00), MaxValueValidator(50000.00)]
    )