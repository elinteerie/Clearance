from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

from .models import DefaultUser, StudentUser

class CustomRegisterSerializer(RegisterSerializer):
    user_type = serializers.ChoiceField(choices=DefaultUser.USER_TYPES)

    def custom_signup(self, request, user):
        user.user_type = self.validated_data.get('user_type')
        user.save()
        if user.user_type == 'STUDENT':
            StudentUser.objects.create(student=user)
        # Add more cases for other user types if needed
        return user
        
        