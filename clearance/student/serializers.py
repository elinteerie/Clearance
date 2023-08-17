from django.contrib.auth import get_user_model
from rest_framework import serializers
from account.models import StudentUser, DefaultUser


User = get_user_model()

class DefaultUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class StudentProfileRetrieveUpdateSerializer(serializers.ModelSerializer):
    student = DefaultUserSerializer()
    class Meta:
        model = StudentUser
        exclude = ['ict_cleared', 'dept_cleared']
        
    def update(self, instance, validated_data):
        # Update the associated DefaultUser fields (first_name and last_name)
        user_data = validated_data.pop('student', {})
        user = instance.student
        for attr, value in user_data.items():
            setattr(user, attr, value)
        user.save()

        # Update the other fields of the StudentUser instance
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance


