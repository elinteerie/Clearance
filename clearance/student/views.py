from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from accounts.models import StudentUser
from .serializers import StudentProfileRetrieveUpdateSerializer


class StudentProfileRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    """
    Retrieve and update the profile of the authenticated student user.

    This view allows an authenticated student user to retrieve and update their profile information,
    excluding the 'ict_cleared' and 'dept_cleared' fields. The student profile instance is associated
    with the authenticated user.

    Serializer:
        StudentProfileRetrieveUpdateSerializer: The serializer used to retrieve and update the student profile.

    Authentication:
        Requires the user to be authenticated.

    HTTP Methods:
        - GET: Retrieve the student profile information.
        - PUT/PATCH: Update the student profile information.

    Returns:
        The serialized student profile instance.
    """
    serializer_class = StudentProfileRetrieveUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """
        Retrieve the student profile associated with the authenticated user.

        Returns:
            The student profile instance associated with the authenticated user.
        """
        student_profile = StudentUser.objects.get(student=self.request.user)
        return student_profile

