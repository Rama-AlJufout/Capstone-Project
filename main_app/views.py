from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
# from .forms import SignUpForm
# from django.contrib.auth import login


def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, 'about.html')

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

from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/register.html', {'form': form})
