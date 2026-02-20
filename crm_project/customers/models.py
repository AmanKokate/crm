from django.db import models


class Customer(models.Model):
    """Customer model for managing customer information"""
    
    class Status(models.TextChoices):
        LEAD = 'LEAD', 'Lead'
        CUSTOMER = 'CUSTOMER', 'Customer'
    
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=255, blank=True)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.LEAD,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} ({self.get_status_display()})"
