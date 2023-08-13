from django.db import models

from account.models import StudentUser

class StudentDocumentICT(models.Model):
    student = models.ForeignKey(StudentUser, on_delete=models.CASCADE, related_name='documents')
    jamb_admission_letter = models.FileField(upload_to='student_documents/student', null=True, blank=True)
    futo_post_ume_result = models.FileField(upload_to='student_documents/student', null=True, blank=True)
    o_level_result = models.FileField(upload_to='student_documents/student', null=True, blank=True)
    confirmation_of_admission =models.FileField(upload_to='student_documents/student', null=True, blank=True)
    futo_admission_letter = models.FileField(upload_to='student_documents/student', null=True, blank=True)
    validity_form = models.FileField(upload_to='student_documents/student', null=True, blank=True)
    acceptance_letter = models.FileField(upload_to='student_documents/student', null=True, blank=True)
    birth_certificate = models.FileField(upload_to='student_documents/student', null=True, blank=True)
    lga_identification = models.FileField(upload_to='student_documents/student', null=True, blank=True)
    school_fees_receipt = models.FileField(upload_to='student_documents/student', null=True, blank=True)
    direct_entry_result = models.FileField(upload_to='student_documents/student', null=True, blank=True)
    submitted = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)

    

class StudentRecord(models.Model):
    student = models.ForeignKey(StudentUser, on_delete=models.CASCADE, related_name='documents_final')
    ictdocs = models.ForeignKey(StudentDocumentICT, on_delete=models.CASCADE, null=True, blank=True, related_name='ictdocss')
    form_1 = models.FileField(upload_to='student_documents/student', null=True, blank=True)
    form_04= models.FileField(upload_to='student_documents/student', null=True, blank=True)
    form_09 = models.FileField(upload_to='student_documents/student', null=True, blank=True)
    form_08 = models.FileField(upload_to='student_documents/student', null=True, blank=True)
    form_12 = models.FileField(upload_to='student_documents/student', null=True, blank=True)
    form_13 =  models.FileField(upload_to='student_documents/student', null=True, blank=True)
    submitted = models.BooleanField(default=False)
    verified =  models.BooleanField(default=False)


    
