from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom User model with role-based access"""
    
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        SALES = 'SALES', 'Sales'
    
    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.SALES,
    )
    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
