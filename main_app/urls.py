from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/update/', views.update_profile_view, name='update_profile'),
    path('profile/password/', auth_views.PasswordChangeView.as_view(template_name='user/set_password.html',success_url='/profile/'), name='password_change'),
    path('activities/', views.activity_log_view, name='activity_log'),
    path('update/<int:pk>/', views.activity_update, name='activity_update'),
    path('delete/<int:pk>/', views.activity_delete, name='activity_delete'),
]