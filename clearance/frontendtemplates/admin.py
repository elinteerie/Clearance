from django.contrib import admin

from .models import FormTemplate

admin.site.site_title ='Clearance Dashboard'
admin.site.site_header ='Clearance Dashboard'
admin.site.register(FormTemplate)
