from django.urls import path, include 
from .views import * 

urlpatterns = [
    path('api/', include('sw_utils.sw_auth.api.urls')),
    path('sw_logout/', sw_logout, name='sw_logout'),
]
