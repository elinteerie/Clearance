from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ScreenUser, StudentUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = ScreenUser
        fields = '__all__'


class CustomUSerChangeForm(UserChangeForm):
    class Meta:
        model = ScreenUser
        fields = '__all__'
        
        
class StudentCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = StudentUser
        fields = '__all__'


class StudentUSerChangeForm(UserChangeForm):
    class Meta:
        model = StudentUser
        fields = '__all__'        
