from django.urls import path
from .views import StudentProfileRetrieveUpdateView, StudentUserRetrieveView, FacultyListView, DepartmentListView

urlpatterns = [
    # ... other URL patterns ...
    path('profile/', StudentUserRetrieveView.as_view(), name='student-profile'),
    path('profile/edit/', StudentProfileRetrieveUpdateView.as_view(), name='student-profile-update'),
    path('faculties/', FacultyListView.as_view(), name='faculty-list'),
    path('departments/',DepartmentListView.as_view(), name='department-list'),
]
