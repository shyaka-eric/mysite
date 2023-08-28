from django .forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
        
from .models import Workout

from .models import Goal

from .models import Progress

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = '__all__'




class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = '__all__'




class ProgressForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = '__all__'

