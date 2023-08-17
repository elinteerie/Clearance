from rest_framework import serializers
from account.models import StudentUser, DefaultUser


class StudentProfileRetrieveUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentUser
        exclude = ['ict_cleared', 'dept_cleared', 'student']


