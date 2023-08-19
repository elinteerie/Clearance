from rest_framework import generics
from .models import StudentUser, ScreenUser
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from dj_rest_auth.views import LoginView
from django.contrib.auth import authenticate

from dj_rest_auth.registration.views import RegisterView


from .serializers import CustomRegisterSerializer, CustomLoginSerializer

class CustomRegisterView(RegisterView):
    """
    Custom registration view that creates a new user profile.

    This view extends the default registration view to create a new user profile
    with additional information like username and user type.

    Serializer:
        CustomRegisterSerializer: The serializer used for user registration.

    HTTP Methods:
        - POST: Create a new user profile with provided data.
            -USER_TYPE FIELD: DAO, STUDENT, SENATE, SAO, UAO, SCREEN - Use STUDENT for registering students
        

    Returns:
        Upon successful registration, returns a response with a status code of 201 (Created)
        and includes the following data:
        - detail: A success message.
        - username: The username of the registered user.
        - user_type: The user type of the registered user.
    """
    serializer_class = CustomRegisterSerializer

    def perform_create(self, serializer):
        """
        Create a new user profile with provided data.

        Args:
            serializer: The serializer instance containing registration data.

        Returns:
            A Response object containing the success message and user information.
        """
        user = serializer.save(self.request)
        response_data = {
            "detail": "Profile successfully created.",
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "user_type": user.user_type,
            }
        }
        return Response(response_data, status=status.HTTP_201_CREATED)


class CustomLoginView(LoginView):
    serializer_class = CustomLoginSerializer
    def login(self, request):
        # Your custom login logic here
        # Example:
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            login(request, user)
            # Return a successful response
            return Response({'message': 'Login successful'})
        else:
            # Return an error response
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)