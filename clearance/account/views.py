from rest_framework import generics
from .models import StudentUser, ScreenUser

from .serializers import StudentUserSerializer, ScreenUserSerializer

class StudentListByScreenUser(generics.ListAPIView):
    serializer_class = StudentUserSerializer
    
    def get_queryset(self):
        # Retrieve the screen user based on the authenticated user
        screen_user = ScreenUser.objects.get(screener=self.request.user)
        
        # Retrieve the students associated with the screen user
        students = screen_user.students.all()
        return students
    
class StudentUpdateByScreenUser(generics.UpdateAPIView):
    serializer_class = StudentUserSerializer

    def get_queryset(self):
        # Retrieve the screen user based on the authenticated user
        screen_user = ScreenUser.objects.get(screener=self.request.user)
        
        # Retrieve the students associated with the screen user
        students = screen_user.students.all()
        return students

class StudentUserDetail(generics.RetrieveAPIView):
    queryset = StudentUser.objects.all()
    serializer_class = StudentUserSerializer

class ScreenUserDetail(generics.RetrieveAPIView):
    queryset = ScreenUser.objects.all()
    serializer_class = ScreenUserSerializer
