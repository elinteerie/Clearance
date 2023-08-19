from django.urls import path, include
from . import views
from .views import CustomRegisterView
from .views import CustomLoginView
from .serializers import CustomLoginSerializer



urlpatterns = [
    #path('auth/login/', CustomLoginView.as_view(), name='custom-login'),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/reg/', CustomRegisterView.as_view(), name='register'),
    path('auth/reg/', include('dj_rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),
] 
    
    
    
