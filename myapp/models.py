from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save




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

@receiver(post_save, sender=settings.AUTH_USER_MODEL )

def create_auth_token(sender, instance = None, created = False,**kwargs):
    if created:
        Token.objects.create(user =instance)
# Create your models here.
