from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLES_CHOICES = (
        ('Admin', 'Admin'),
        ('User', 'User'),
    )

    role = models.CharField(max_length=10, choices=ROLES_CHOICES, default='User')

    def __str__(self):
        return f"{self.username} ({self.role})"

# Create your models here.
