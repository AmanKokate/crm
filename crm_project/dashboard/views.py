from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from leads.models import Lead
from customers.models import Customer


class DashboardView(APIView):
    """
    API endpoint for dashboard statistics
    Returns: total_leads, converted_leads, total_customers, conversion_rate
    """
    
    def get(self, request):
        """Get dashboard statistics"""
        # Count total leads
        total_leads = Lead.objects.count()
        
        # Count converted leads
        converted_leads = Lead.objects.filter(status=Lead.Status.CONVERTED).count()
        
        # Count total customers (excluding soft-deleted ones)
        total_customers = Customer.objects.filter(is_deleted=False).count()
        
        # Calculate conversion rate
        if total_leads > 0:
            conversion_rate = round((converted_leads / total_leads) * 100, 2)
        else:
            conversion_rate = 0.0
        
        data = {
            'total_leads': total_leads,
            'converted_leads': converted_leads,
            'total_customers': total_customers,
            'conversion_rate': conversion_rate
        }
        
        return Response(data, status=status.HTTP_200_OK)
