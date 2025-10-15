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

    profile_image = models.URLField(
        max_length=200,
        blank=True,
        null=True,
    )

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

class MealLog(models.Model):
    MEAL_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='meal_logs')
    meal_type = models.CharField(max_length=20, choices=MEAL_CHOICES)
    food_items = models.TextField(help_text="List your food items, separated by commas")
    calories = models.PositiveIntegerField()
    date = models.DateField(help_text="The date of this meal")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.meal_type} on {self.date} ({self.calories} cal)"


class JournalEntry(models.Model):
    MOOD_CHOICES = [
        ('happy', 'Happy'),
        ('sad', 'Sad'),
        ('angry', 'Angry'),
        ('anxious', 'Anxious'),
        ('calm', 'Calm'),
        ('excited', 'Excited'),
        ('tired', 'Tired'),
        ('neutral', 'Neutral'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='journal_entries')
    mood = models.CharField(max_length=20, choices=MOOD_CHOICES)
    note = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.mood} on {self.date}"