from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ScreenUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = ScreenUser
        fields = '__all__'


class CustomUSerChangeForm(UserChangeForm):
    class Meta:
        model = ScreenUser
        fields = '__all__'