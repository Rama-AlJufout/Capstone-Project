from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'age', 'height', 'weight', 'gender']


class CustomUserUpdate(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'age', 'height', 'weight', 'gender']
