from django.shortcuts import render, redirect, get_object_or_404
from .models import ActivityLog
from .forms import CustomUserCreationForm, CustomUserUpdate, ActivityLogForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import SetPasswordForm
# from .forms import SignUpForm
# from django.contrib.auth import login


def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, 'about.html')

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
    user = request.user
    activities = ActivityLog.objects.filter(user=user).order_by('-date')
    return render(request, 'user/profile.html', {'user': user, 'activities': activities})

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

@login_required
def activity_log_view(request):
    # Create + Read
    user = request.user
    activities = ActivityLog.objects.filter(user=user).order_by('-date')
    
    if request.method == 'POST':
        form = ActivityLogForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.user = user
            activity.save()
            messages.success(request, 'Activity logged successfully!')
            return redirect('activity_log')
    else:
        form = ActivityLogForm()
    
    return render(request, 'activity/activity_log.html', {'form': form, 'activities': activities })

@login_required
def activity_update(request, pk):
    # Update
    activity = get_object_or_404(ActivityLog, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = ActivityLogForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            messages.success(request, 'Activity updated successfully!')
            return redirect('activity_log')
    else:
        form = ActivityLogForm(instance=activity)
    
    return render(request, 'activity/activity_form.html', {
        'form': form,
        'activity': activity,
        'title': 'Edit Activity'
    })

@login_required
def activity_delete(request, pk):
    # Delete
    activity = get_object_or_404(ActivityLog, pk=pk, user=request.user)
    
    if request.method == 'POST':
        activity.delete()
        messages.success(request, f'Activity "{activity.get_activity_type_display}" deleted successfully!')
        return redirect('activity_log')
    
    return render(request, 'activity/activity_confirm_delete.html', {
        'activity': activity
    })