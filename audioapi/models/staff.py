from django.db import models
from django.contrib.auth.models import User

class Staff(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    bio = models.TextField()
    isAvailable = models.BooleanField(default=True)

    