from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

from .models import DefaultUser

class CustomRegisterSerializer(RegisterSerializer):
    user_type = serializers.ChoiceField(choices=DefaultUser.USER_TYPES)

    def custom_signup(self, request, user):
        user.user_type = self.validated_data.get('user_type')
        user.save()