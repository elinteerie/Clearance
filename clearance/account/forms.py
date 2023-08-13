from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import DefaultUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = DefaultUser
        fields = '__all__'


class CustomUSerChangeForm(UserChangeForm):
    class Meta:
        model = DefaultUser
        fields = '__all__'
        