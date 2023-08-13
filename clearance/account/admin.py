from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (DefaultUser, StudentUser, ScreenUser, UAOUser, DAOUser, SAOUser, 
                     Faculty, Department, Current_Admission_Session, SenateUser)
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import CustomUserCreationForm, CustomUSerChangeForm
from django.urls import path
from django.shortcuts import redirect





class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUSerChangeForm
    model = DefaultUser

    list_display = [
                    "username",
                    "email",
                    "is_staff"]
    fieldsets = UserAdmin.fieldsets+((None, {"fields": ()}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ()}),)


class StudentInline(admin.TabularInline):
    model = ScreenUser.students.through
    extra = 1

class ScreenUserAdmin(admin.ModelAdmin):
    inlines = [StudentInline]
    list_display = ('screener', 'department', 'faculty')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj:
            form.base_fields['students'].queryset = obj.students.all()
        return form

admin.site.register(ScreenUser, ScreenUserAdmin)






admin.site.register(DefaultUser, CustomUserAdmin)
admin.site.register(Department)
admin.site.register(StudentUser)
admin.site.register(SAOUser)
admin.site.register(DAOUser)
admin.site.register(UAOUser)
#admin.site.register(ScreenUser)
admin.site.register(Faculty)
admin.site.register(Current_Admission_Session)
admin.site.register(SenateUser)

