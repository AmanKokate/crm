from django.contrib import admin
from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    """Admin configuration for Lead model"""
    
    list_display = ['name', 'email', 'phone', 'status', 'assigned_to', 'created_at']
    list_filter = ['status', 'created_at', 'assigned_to']
    search_fields = ['name', 'email', 'phone']
    ordering = ['-created_at']
    list_select_related = ['assigned_to']
