from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (StudentUser, ScreenUser, UAOUser, DAOUser, SAOUser, 
                     Faculty, Department, Current_Admission_Session, SenateUser)
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import CustomUserCreationForm, CustomUSerChangeForm, StudentCreationForm, StudentUSerChangeForm





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
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:  # Superusers see all students
            return qs
        elif request.user.department:  # Non-superusers filter by department
            return qs.filter(department=request.user.department)
        return qs.none()  # Hide students if no department set
    
    
class StudentUserAdmin(UserAdmin):
    add_form = StudentCreationForm
    form = StudentUSerChangeForm
    model = StudentUser

    list_display = [
                    "username",
                    "first_name",
                    "department",
                    "faculty"]
    fieldsets = UserAdmin.fieldsets+((None, {"fields": ("department", "faculty", "nationality", 'place_of_birth','state_of_origin', 'local_government')}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("department", "faculty",)}),)
    
    


class UAOUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    # Add more fields if needed


admin.site.register(StudentUser, StudentUserAdmin)
admin.site.register(ScreenUser, CustomUserAdmin)
admin.site.register(UAOUser, UserAdmin)
admin.site.register(DAOUser, UserAdmin)
admin.site.register(SAOUser, UserAdmin)
admin.site.register(Department)
admin.site.register(Faculty)
admin.site.register(Current_Admission_Session)
admin.site.register(SenateUser)

