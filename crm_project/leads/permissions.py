from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission:
    - Admin users have full access
    - Sales users have read/write access but cannot delete
    """
    
    def has_permission(self, request, view):
        # Allow authenticated users
        if not request.user or not request.user.is_authenticated:
            return False
        
        # Admin can do anything
        if request.user.role == 'ADMIN':
            return True
        
        # Sales cannot delete
        if request.user.role == 'SALES' and view.action == 'destroy':
            return False
        
        # Sales can do other actions (list, retrieve, create, update)
        return True
