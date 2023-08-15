from rest_framework import serializers
from .models import StudentUser, ScreenUser
from document.models import StudentDocumentICT, StudentRecord

class StudentDocumentICTSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = StudentDocumentICT
        fields = '__all__'
        
    def update(self, instance, validated_data):
        instance.submitted = validated_data.get('submitted', instance.submitted)
        instance.verified = validated_data.get('verified', instance.verified)
        instance.save()
        return instance
        
        
class StudentRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentRecord
        fields = '__all__'
    

class StudentUserSerializer(serializers.ModelSerializer):
    document = StudentDocumentICTSerializer(read_only=True)
    records = StudentRecordSerializer(read_only=True)
    
    class Meta:
        model = StudentUser
        fields = '__all__' 
        depth = 1
        
        
    def update(self, instance, validated_data):
        document_data = validated_data.pop('document', {})
        instance = super().update(instance, validated_data)
        document_serializer = self.fields['document']
        document_instance = instance.document
        document_serializer.update(document_instance, document_data)
        return instance

class ScreenUserSerializer(serializers.ModelSerializer):
    
    students = StudentUserSerializer(many=True, read_only=True)
    
    class Meta:
        model = ScreenUser
        fields = '__all__'
