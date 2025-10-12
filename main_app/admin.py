from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, ActivityLog

# Register your custom user model
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Fields to display in the user list page
    list_display = ('username', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')

    # Fields displayed when editing a user
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Fields displayed when adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

    # Search box in the admin user list
    search_fields = ('username',)
    # Default ordering by username
    ordering = ('username',)

# Register the model with the admin
admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_type', 'duration_minutes', 'calories_burned', 'date')
    search_fields = ('user__username', 'activity_type')
    list_filter = ('activity_type', 'date')
