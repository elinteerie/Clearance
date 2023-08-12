from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (StudentUser, ScreenUser, UAOUser, DAOUser, SAOUser, 
                     Faculty, Department, Current_Admission_Session, SenateUser)
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import CustomUserCreationForm, CustomUSerChangeForm





class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUSerChangeForm
    model = ScreenUser

    list_display = [
                    "username",
                    "email",
                    "department",
                    "is_staff"]
    fieldsets = UserAdmin.fieldsets+((None, {"fields": ("department", "faculty",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("department", "faculty",)}),)
    
    


class UAOUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    # Add more fields if needed


admin.site.register(StudentUser, CustomUserAdmin)
admin.site.register(ScreenUser, CustomUserAdmin)
admin.site.register(UAOUser, UserAdmin)
admin.site.register(DAOUser, UserAdmin)
admin.site.register(SAOUser, UserAdmin)
admin.site.register(Department)
admin.site.register(Faculty)
admin.site.register(Current_Admission_Session)
admin.site.register(SenateUser)

