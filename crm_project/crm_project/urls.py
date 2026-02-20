"""
URL configuration for crm_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Import ViewSets
from customers.views import CustomerViewSet
from leads.views import LeadViewSet
from users.views import UserRegistrationView
from dashboard.views import DashboardView

# Create router and register ViewSets
router = DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='customer')
router.register(r'leads', LeadViewSet, basename='lead')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/users/register/", UserRegistrationView.as_view(), name="user-register"),
    path("api/dashboard/", DashboardView.as_view(), name="dashboard"),
    path("api/", include(router.urls)),
]
