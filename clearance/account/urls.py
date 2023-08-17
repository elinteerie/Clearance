from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('api/students/', views.StudentListByScreenUser.as_view(), name='student-list'),
    path('api/students/<int:pk>/', views.StudentUserDetail.as_view(), name='student-detail'),
    path('api/screen-users/', views.ScreenUserDetail.as_view(), name='screen-user-detail'),
    path('api/students/u/<str:username>/', views.StudentUpdateByScreenUser.as_view(), name='student-detail'),
    path('update/<int:pk>/', views.StudentDocumentICTUpdateByScreenUser.as_view(), name='update-student-document-ict'),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/reg/', include('dj_rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),
] 
    
    
    
