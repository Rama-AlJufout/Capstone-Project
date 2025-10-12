from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, ActivityLog

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'age', 'height', 'weight', 'gender']


class CustomUserUpdate(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'age', 'height', 'weight', 'gender']



class ActivityLogForm(forms.ModelForm):
    class Meta:
        model = ActivityLog
        fields = ['activity_type', 'start_time', 'end_time', 'calories_burned']
        widgets = {
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
            'activity_type': forms.Select(attrs={'class': 'form-select'}),
        }
