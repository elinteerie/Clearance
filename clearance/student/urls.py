from django.urls import path
from .views import StudentProfileRetrieveUpdateView, StudentUserRetrieveView

urlpatterns = [
    # ... other URL patterns ...
    path('profile/', StudentUserRetrieveView.as_view(), name='student-profile'),
    path('profile/edit/', StudentProfileRetrieveUpdateView.as_view(), name='student-profile-update'),
]
