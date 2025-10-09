from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


# class SignUpForm (UserCreationForm):
#     age = forms.IntegerField(required=False)
#     gender = forms.CharField(max_length=10, required=False)
#     height = forms.FloatField(required=False)
#     weight = forms.FloatField(required=False)

#     class Meta:
#         model = User
#         fields = ('username', 'age', 'gender', 'height', 'weight', 'password1', 'password2')