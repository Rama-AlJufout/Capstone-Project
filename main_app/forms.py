from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, ActivityLog, MealLog, JournalEntry

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

class MealLogForm(forms.ModelForm):
    class Meta:
        model = MealLog
        fields = ['meal_type', 'food_items', 'calories', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'food_items': forms.Textarea(attrs={'rows': 3}),
        }

class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ['mood', 'note']
        widgets = {
            'mood': forms.Select(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }