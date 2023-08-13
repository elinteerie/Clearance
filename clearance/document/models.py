from django.db import models

from account.models import StudentUser

class StudentDocumentICT(models.Model):
    student = models.ForeignKey(StudentUser, on_delete=models.CASCADE, related_name='documents')
    jamb_admission_letter = models.FileField(upload_to='student_documents/student')
    futo_post_ume_result = models.FileField(upload_to='student_documents/student')
    o_level_result = models.FileField(upload_to='student_documents/student')
    confirmation_of_admission = models.FileField(upload_to='student_documents/student')
    futo_admission_letter = models.FileField(upload_to='student_documents/student')
    validity_form = models.FileField(upload_to='student_documents/student')
    acceptance_letter = models.FileField(upload_to='student_documents/student')
    birth_certificate = models.FileField(upload_to='student_documents/student')
    lga_identification = models.FileField(upload_to='student_documents/student')
    school_fees_receipt = models.FileField(upload_to='student_documents/student')
    direct_entry_result = models.FileField(upload_to='student_documents/student', null=True, blank=True)
    

    
