from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('api/students/', views.StudentListByScreenUser.as_view(), name='student-list'),
    path('api/students/<int:pk>/', views.StudentUserDetail.as_view(), name='student-detail'),
    path('api/screen-users/<int:pk>/', views.ScreenUserDetail.as_view(), name='screen-user-detail'),
    path('api/students/u/<int:pk>/', views.StudentUpdateByScreenUser.as_view(), name='student-detail'),
    
] 
    
    
    
