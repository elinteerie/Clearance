from rest_framework import serializers
from account.models import StudentUser, ScreenUser
from document.models import StudentDocumentICT, StudentRecord

class StudentDocumentICTSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = StudentDocumentICT
        fields = fields = ['jamb_admission_letter', 'futo_post_ume_result', 'o_level_result', 'confirmation_of_admission', 'futo_admission_letter', 'validity_form', 'acceptance_letter', 'birth_certificate', 'lga_identification', 'school_fees_receipt', 'direct_entry_result', 'submitted', 'verified']
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

        
        
class StudentRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentRecord
        fields = '__all__'
    

class StudentUserSerializer(serializers.ModelSerializer):
    document = StudentDocumentICTSerializer()
    #records = StudentRecordSerializer(read_only=True)
    username = serializers.CharField(source='studentuser.username', read_only=True)
    
    class Meta:
        model = StudentUser
        fields = '__all__' 
        depth = 2
        
    def update(self, instance, validated_data):
        document_data = validated_data.pop('document', {})
        document_instance = instance.document

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        for attr, value in document_data.items():
            setattr(document_instance, attr, value)

        instance.save()
        document_instance.save()
        return instance
    
        
    

        

class ScreenUserSerializer(serializers.ModelSerializer):
    
    students = StudentUserSerializer(many=True, read_only=True)
    
    class Meta:
        model = ScreenUser
        fields = '__all__'
        
    
        
        
class ScreenUserSerializeraa(serializers.ModelSerializer):
    
    #students = StudentUserSerializer(many=True, read_only=True)
    
    class Meta:
        model = ScreenUser
        fields = '__all__'
        
        depth = 1


class StudentDocumentICTUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDocumentICT
        fields = ['jamb_admission_letter', 'futo_post_ume_result', 'o_level_result', 'confirmation_of_admission', 'futo_admission_letter', 'validity_form', 'acceptance_letter', 'birth_certificate', 'lga_identification', 'school_fees_receipt', 'direct_entry_result', 'submitted', 'verified']
