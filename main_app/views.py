from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm
from django.contrib.auth import login


def home(request):
    return HttpResponse('<h1>Hello Rama</h1>')

def about(request):
    return HttpResponse('<h1> About Rama </h1>')

# def signup_view(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)  # Log in the user after signup
#             return redirect('home')
#     else:
#         form = SignUpForm()
#     return render(request, 'main_app/signup.html', {'form': form})