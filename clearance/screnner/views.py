from django.shortcuts import render

from rest_framework import generics
from accounts.models import StudentUser, ScreenUser
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .serializers import StudentUserSerializer, ScreenUserSerializer, ScreenUserSerializeraa, StudentDocumentICTSerializer, StudentDocumentICTUpdateSerializer
from document.models import StudentDocumentICT
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


class StudentListByScreenUser(generics.ListAPIView):
    """
    Retrieve a list of students associated with the authenticated ScreenUser.

    This view returns a list of students associated with the ScreenUser who is
    currently authenticated. The ScreenUser is determined based on the authenticated user.
    Students are filtered based on the screen user's association.

    Serializer:
        StudentUserSerializer: The serializer used to represent the student instances.

    Authentication:
        Requires the user to be authenticated.

    HTTP Methods:
        - GET: Retrieve the list of students associated with the authenticated ScreenUser.

    Returns:
        A list of serialized student instances.
    """
    serializer_class = StudentUserSerializer
    
    def get_queryset(self):
        # Retrieve the screen user based on the authenticated user
        screen_user = ScreenUser.objects.get(screener=self.request.user)
        
        # Retrieve the students associated with the screen user
        students = screen_user.students.all()
        return students
    
    
class StudentUpdateByScreenUser(generics.RetrieveUpdateAPIView):
    """
    Update the fields of a student associated with the authenticated ScreenUser.

    This view allows an authenticated ScreenUser to update the fields of a specific student.
    The ScreenUser's association with the student is determined based on the authenticated user.
    The student instance is retrieved using the provided primary key.

    Serializer:
        StudentUserSerializer: The serializer used to represent the student instance.

    Authentication:
        Requires the user to be authenticated.

    HTTP Methods:
        - GET: Retrieve the student instance associated with the authenticated ScreenUser.
        - PUT/PATCH: Update the fields of the student instance.

    Parameters:
        - username (regnum): The primary key of the student instance.

    Returns:
        The updated serialized student instance.
    """
    serializer_class = StudentUserSerializer

    def get_object(self):
        """
        Retrieve the student associated with the authenticated ScreenUser.

        Returns:
            The student instance associated with the ScreenUser.
        """
        # Retrieve the student associated with the screen user
        screen_user = ScreenUser.objects.get(screener=self.request.user)
        
        # Retrieve the student using the username
        student_username = self.kwargs['username']  # Assuming you're passing 'username' in the URL kwargs
        student = screen_user.students.get(student__username=student_username)
        
        return student
    
class StudentUserDetail(generics.RetrieveAPIView):
    queryset = StudentUser.objects.all()
    serializer_class = StudentUserSerializer

class ScreenUserDetail(generics.RetrieveAPIView):
    """
    Retrieve details of the currently logged-in ScreenUser.

    This view retrieves the information of the ScreenUser who is currently logged in.
    It is intended to provide detailed information about the logged-in ScreenUser.
    Only authenticated users can access this view.

    Attributes:
        serializer_class (class): The serializer class used to serialize the ScreenUser data.

    Methods:
        dispatch(*args, **kwargs): Ensure authentication and call the parent dispatch method.
        get_object(): Retrieve the ScreenUser based on the logged-in user.

    Example:
        To retrieve the details of the currently logged-in ScreenUser,
        make a GET request to this endpoint.

    """

    serializer_class = ScreenUserSerializeraa
    
    @method_decorator(login_required)  # Use this decorator to ensure the user is logged in
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get_object(self):
        """
        Retrieve the ScreenUser object for the currently logged-in user.
        
        Returns:
            ScreenUser: The ScreenUser instance of the logged-in user.
        
        Raises:
            Http404: If the ScreenUser for the logged-in user does not exist.
        """
        # Retrieve the ScreenUser based on the logged-in user
        return ScreenUser.objects.get(screener=self.request.user)
    
class StudentDocumentICTUpdateByScreenUser(generics.UpdateAPIView):
    serializer_class = StudentDocumentICTUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Retrieve the StudentDocumentICT instances associated with the logged-in ScreenUser's students
        screen_user = ScreenUser.objects.get(screener=self.request.user)
        students = screen_user.students.all()
        return StudentDocumentICT.objects.filter(student__in=students)
