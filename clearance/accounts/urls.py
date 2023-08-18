from django.urls import path, include
from . import views


urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/reg/', include('dj_rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),
] 
    
    
    
