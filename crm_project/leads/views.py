from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Lead
from .serializers import LeadSerializer
from .permissions import IsAdminOrReadOnly


class LeadViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Lead model with role-based access control
    - Admin: Full access to all leads
    - Sales: Can only see and manage their assigned leads, cannot delete
    """
    serializer_class = LeadSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status', 'assigned_to']
    search_fields = ['name', 'email', 'phone']
    ordering_fields = ['created_at']
    ordering = ['-created_at']
    
    def get_queryset(self):
        """
        Filter queryset based on user role:
        - Admin users can see all leads
        - Sales users can only see leads assigned to them
        """
        user = self.request.user
        
        if user.role == 'ADMIN':
            # Admin can see all leads
            return Lead.objects.all()
        elif user.role == 'SALES':
            # Sales can only see leads assigned to them
            return Lead.objects.filter(assigned_to=user)
        
        # Default: return empty queryset for safety
        return Lead.objects.none()
