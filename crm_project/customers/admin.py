from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """Admin configuration for Customer model"""
    
    list_display = ['name', 'email', 'phone', 'company', 'status', 'created_at', 'is_deleted']
    list_filter = ['status', 'is_deleted', 'created_at']
    search_fields = ['name', 'email', 'phone', 'company']
    ordering = ['-created_at']
