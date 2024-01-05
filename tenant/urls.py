# real_estate/urls.py

from django.urls import path
from .views import property_list, tenant_list

urlpatterns = [
    
    path('tenants/', tenant_list, name='tenant-list'),
    # Add more URLs as needed
]
