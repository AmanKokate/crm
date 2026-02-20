from rest_framework import serializers
from .models import Lead
from django.contrib.auth import get_user_model

User = get_user_model()


class LeadSerializer(serializers.ModelSerializer):
    """Serializer for Lead model"""
    
    assigned_to_username = serializers.CharField(source='assigned_to.username', read_only=True)
    
    class Meta:
        model = Lead
        fields = ['id', 'name', 'email', 'phone', 'status', 'assigned_to', 'assigned_to_username', 'created_at']
        read_only_fields = ['id', 'created_at']
