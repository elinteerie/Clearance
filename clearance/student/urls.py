from django.urls import path
from .views import StudentProfileRetrieveUpdateView

urlpatterns = [
    # ... other URL patterns ...
    path('profile/edit/', StudentProfileRetrieveUpdateView.as_view(), name='student-profile-update'),
]
