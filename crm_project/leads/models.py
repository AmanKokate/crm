from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Lead(models.Model):
    """Lead model for managing potential customers"""
    
    class Status(models.TextChoices):
        NEW = 'NEW', 'New'
        CONTACTED = 'CONTACTED', 'Contacted'
        CONVERTED = 'CONVERTED', 'Converted'
    
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    status = models.CharField(
        max_length=15,
        choices=Status.choices,
        default=Status.NEW,
    )
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='leads'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} ({self.get_status_display()})"
