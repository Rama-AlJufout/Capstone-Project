from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserUpdate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import SetPasswordForm
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


@login_required
def profile_view(request):
    user = request.user  # Get the logged-in user
    context = {
        'user': user
    }
    return render(request, 'user/profile.html', context)

@login_required
def update_profile_view(request):
    user = request.user
    if request.method == 'POST':
        form = CustomUserUpdate(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserUpdate(instance=user)
    
    return render(request, 'user/update.html', {'form': form})

@login_required
def set_password_view(request):
    if request.method == 'POST':
        form = SetPasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = SetPasswordForm(request.user)
    return render(request, 'user/set_password.html', {'form': form})