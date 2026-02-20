from rest_framework import permissions


class IsAdminUser(permissions.BasePermission):
    """
    Permission to only allow users with ADMIN role.
    """
    
    def has_permission(self, request, view):
        # Check if user is authenticated and has ADMIN role
        return (
            request.user 
            and request.user.is_authenticated 
            and request.user.role == 'ADMIN'
        )


class IsSalesUser(permissions.BasePermission):
    """
    Permission to only allow users with SALES role.
    """
    
    def has_permission(self, request, view):
        # Check if user is authenticated and has SALES role
        return (
            request.user 
            and request.user.is_authenticated 
            and request.user.role == 'SALES'
        )


class LeadOwnerPermission(permissions.BasePermission):
    """
    Permission to only allow assigned users to update a lead.
    """
    
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any authenticated user
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the assigned user or admin
        if request.user.role == 'ADMIN':
            return True
        
        # Check if the user is the one assigned to the lead
        return obj.assigned_to == request.user
