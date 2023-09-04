from django.contrib.auth import get_user_model
from rest_framework import serializers
from accounts.models import StudentUser, DefaultUser, Department, Faculty


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
    
class StudentUserSerializering(serializers.ModelSerializer):
    class Meta:
        model = StudentUser
        fields = "__all__"
        #read_only = ['student']
        depth  = 1




class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class FacultySerializer(serializers.ModelSerializer):
    departments = DepartmentSerializer(many=True, read_only=True)

    class Meta:
        model = Faculty
        fields = '__all__'
