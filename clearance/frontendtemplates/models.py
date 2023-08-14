from django.db import models

class FormTemplate(models.Model):
    form_1 = models.TextField(null=True, blank=True)
    form_08 = models.TextField(null=True, blank=True)
    form_09 = models.TextField(null=True, blank=True)
    form_12 = models.TextField(null=True, blank=True)
    form_13 =  models.TextField(null=True, blank=True)
