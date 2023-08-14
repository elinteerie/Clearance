from django.db import models
from account.models import StudentUser
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import filesizeformat
from django.core.validators import FileExtensionValidator




def validate_file_size(value):
    # 2 MB in bytes
    max_size = 2 * 1024 * 1024
    
    if value.size > max_size:
        raise ValidationError(f"File size must not exceed {filesizeformat(max_size)}.")

def student_document_upload_path(instance, filename):
    # 'instance' is the model instance (StudentDocumentICT or StudentRecord)
    # 'filename' is the uploaded file's name
    return f'media/student_document/{instance.student.student.username}/{filename}'

file_extension_validator = FileExtensionValidator(allowed_extensions=['pdf', 'png', 'jpeg', 'jpg'],
                                                      message='Only PDF, PNG, JPEG, and JPG files are allowed.')

class StudentDocumentICT(models.Model):
    student = models.ForeignKey(StudentUser, on_delete=models.CASCADE, related_name='documents')
    jamb_admission_letter = models.FileField(upload_to=student_document_upload_path, null=True, blank=True, validators=[validate_file_size, file_extension_validator])
    futo_post_ume_result = models.FileField(upload_to=student_document_upload_path, null=True, blank=True, validators=[validate_file_size, file_extension_validator])
    o_level_result = models.FileField(upload_to=student_document_upload_path, null=True, blank=True, validators=[validate_file_size, file_extension_validator])
    confirmation_of_admission = models.FileField(upload_to=student_document_upload_path, null=True, blank=True, validators=[validate_file_size, file_extension_validator])
    futo_admission_letter = models.FileField(upload_to=student_document_upload_path, null=True, blank=True, validators=[validate_file_size, file_extension_validator])
    validity_form = models.FileField(upload_to=student_document_upload_path, null=True, blank=True,validators=[validate_file_size, file_extension_validator])
    acceptance_letter = models.FileField(upload_to=student_document_upload_path, null=True, blank=True, validators=[validate_file_size, file_extension_validator])
    birth_certificate = models.FileField(upload_to=student_document_upload_path, null=True, blank=True, validators=[validate_file_size, file_extension_validator])
    lga_identification =models.FileField(upload_to=student_document_upload_path, null=True, blank=True, validators=[validate_file_size, file_extension_validator])
    school_fees_receipt = models.FileField(upload_to=student_document_upload_path, null=True, blank=True, validators=[validate_file_size, file_extension_validator])
    direct_entry_result = models.FileField(upload_to=student_document_upload_path, null=True, blank=True, validators=[validate_file_size, file_extension_validator])
    submitted = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    
    
    def save(self, *args, **kwargs):
        # Check if all file fields are not blank
        all_files_uploaded = all(getattr(self, field_name) for field_name in [
            'jamb_admission_letter', 'futo_post_ume_result', 'o_level_result',
            'confirmation_of_admission', 'futo_admission_letter', 'validity_form',
            'acceptance_letter', 'birth_certificate', 'lga_identification',
            'school_fees_receipt', 'direct_entry_result'
        ])
        
        
        # Set submitted field to True if all files are uploaded
        if all_files_uploaded:
            self.submitted = True
        
        super().save(*args, **kwargs)






    
    

    

class StudentRecord(models.Model):
    student = models.ForeignKey(StudentUser, on_delete=models.CASCADE, related_name='documents_final')
    ictdocs = models.ForeignKey(StudentDocumentICT, on_delete=models.CASCADE, null=True, blank=True, related_name='ictdocss')
    form_1 = models.FileField(upload_to=student_document_upload_path, null=True, blank=True, validators=[validate_file_size, file_extension_validator])
    form_04= models.FileField(upload_to=student_document_upload_path, null=True, blank=True, validators=[validate_file_size, file_extension_validator])
    form_09 = models.FileField(upload_to=student_document_upload_path, null=True, blank=True, validators=[validate_file_size, file_extension_validator])
    form_08 = models.FileField(upload_to=student_document_upload_path, null=True, blank=True, validators=[validate_file_size, file_extension_validator])
    form_12 = models.FileField(upload_to=student_document_upload_path, null=True, blank=True, validators=[validate_file_size, file_extension_validator])
    form_13 =  models.FileField(upload_to=student_document_upload_path, null=True, blank=True, validators=[validate_file_size, file_extension_validator])
    submitted = models.BooleanField(default=False)
    verified =  models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if all([getattr(self, field) for field in ['form_1', 'form_04', 'form_09', 'form_08', 'form_12', 'form_13']]):
            self.submitted = True
        super(StudentRecord, self).save(*args, **kwargs)


@receiver(post_save, sender=StudentUser)
def create_student_document(sender, instance, created, **kwargs):
    if created:
        StudentDocumentICT.objects.create(student=instance)
post_save.connect(create_student_document, sender=StudentUser)


@receiver(post_save, sender=StudentDocumentICT)
def create_student_record(sender, instance, created, **kwargs):
    if created:
        StudentRecord.objects.create(student=instance.student, ictdocs=instance)
post_save.connect(create_student_record, sender=StudentDocumentICT)



