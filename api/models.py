from django.db import models
from django.contrib.auth.models import User




class Progress(models.Model):
    date = models.DateField()
    measurement = models.DecimalField(max_digits=8, decimal_places=2)
    notes = models.TextField()

    def __str__(self):
        return f"Progress on {self.date}"





class Goal(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    target_date = models.DateField()

    def __str__(self):
        return self.title





class Workout(models.Model):
    exercise = models.CharField(max_length=100)
    duration_minutes = models.PositiveIntegerField()
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.exercise



# Create your models here.
