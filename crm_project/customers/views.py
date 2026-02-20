from rest_framework import viewsets, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Customer
from .serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Customer model with soft delete functionality
    """
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status']
    search_fields = ['name', 'email']
    ordering_fields = ['created_at']
    ordering = ['-created_at']
    
    def get_queryset(self):
        """Return only non-deleted customers"""
        return Customer.objects.filter(is_deleted=False)
    
    def destroy(self, request, *args, **kwargs):
        """Soft delete - set is_deleted to True instead of actual deletion"""
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response(
            {'message': 'Customer deleted successfully'},
            status=status.HTTP_204_NO_CONTENT
        )
