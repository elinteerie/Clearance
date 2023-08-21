from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _


from .models import DefaultUser, StudentUser, DAOUser, SAOUser, SenateUser, UAOUser, ScreenUser
from dj_rest_auth.serializers import LoginSerializer
from django.contrib.auth import authenticate, login

class CustomRegisterSerializer(RegisterSerializer):
    user_type = serializers.ChoiceField(choices=DefaultUser.USER_TYPES)

    def custom_signup(self, request, user):
        user.user_type = self.validated_data.get('user_type')
        user.save()
        if user.user_type == 'STUDENT':
            StudentUser.objects.create(student=user)
        if user.user_type == 'DAO':
            DAOUser.objects.create(dao=user)
        if user.user_type == 'SAO':
            SAOUser.objects.create(sao=user)
        if user.user_type == 'SENATE':
            SenateUser.objects.create(senate=user)
        if user.user_type == 'UAO':
            UAOUser.objects.create(uao=user)
        if user.user_type == 'SCREEN':
            ScreenUser.objects.create(screener=user)
        
        # Add more cases for other user types if needed
        return user
    
    
class CustomLoginSerializer(LoginSerializer):
    username = serializers.CharField(required=True)
    

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise serializers.ValidationError(msg)
            else:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg)
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg)

        attrs['user'] = user
        return attrs
    
    def get_fields(self):
        fields = super().get_fields()
        fields.pop('email')  # Remove the email field from the serializer
        return fields