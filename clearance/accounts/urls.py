from django.urls import path, include
from . import views
from .views import CustomRegisterView
from dj_rest_auth.views import LoginView
from .serializers import CustomLoginSerializer



urlpatterns = [
    path('auth/login/', LoginView.as_view(serializer_class=CustomLoginSerializer), name='login'),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/reg/', CustomRegisterView.as_view(), name='register'),
    path('auth/reg/', include('dj_rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),
] 
    
    
    
