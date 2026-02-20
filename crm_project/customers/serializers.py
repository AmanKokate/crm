from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    """Serializer for Customer model"""
    
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'phone', 'company', 'status', 'created_at', 'is_deleted']
        read_only_fields = ['id', 'created_at', 'is_deleted']
