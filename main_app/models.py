from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import timedelta
from django.utils import timezone

class CustomUser(AbstractUser):
    # Extra fields for health tracking
    age = models.PositiveIntegerField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True, help_text="Height in cm")
    weight = models.FloatField(null=True, blank=True, help_text="Weight in kg")
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.username


class ActivityLog(models.Model):
    ACTIVITY_CHOICES = [
        ('Walking', '🚶 Walking'),
        ('Jump_rope', '🤾 Jump Rope'),
        ('Dancing', '💃 Dancing'),
        ('Running', '🏃 Running'),
        ('Cycling', '🚴 Cycling'),
        ('Yoga', '🧘 Yoga'),
        ('Gym', '🏋️ Gym Workout'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50, choices=ACTIVITY_CHOICES)
    start_time = models.TimeField(default=timezone.now)
    end_time = models.TimeField(default=timezone.now)
    calories_burned = models.PositiveIntegerField(help_text="Calories burned (kcal)")
    date = models.DateField(auto_now_add=True)

    def duration_minutes(self):
        start = timedelta(hours=self.start_time.hour, minutes=self.start_time.minute)
        end = timedelta(hours=self.end_time.hour, minutes=self.end_time.minute)
        return int((end - start).total_seconds() / 60)

    def __str__(self):
        return f"{self.user.username} - {self.get_activity_type_display()} ({self.date})"

