from django.shortcuts import render, redirect
from .models import Workout, Goal, Progress

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .forms import WorkoutForm, GoalForm, ProgressForm


from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required




def index(request):
    user_id = request.user.id
    context = {'user_id': user_id}
    return render(request, 'index.html', context)


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user),
            return redirect('login')
      
    context = {'form':form}
    return render(request, 'register.html', context)


from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def loginPage(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to the 'index' page upon successful login
        else:
            messages.error(request, 'Username or password is incorrect')
            return redirect("login")
    else:
        return render(request, 'login.html')








#@login_required(login_url='login') Put this at every page you want user to view while loged in
def logoutUser(request):
    logout(request)
    return redirect('index')



class WorkoutCreateView(CreateView):
    model = Workout
    form_class = WorkoutForm
    template_name = 'workout/workout_form.html'
    success_url = reverse_lazy('workout_list')




class WorkoutListView(ListView):
    model = Workout
    template_name = 'workout/workout_list.html'



class WorkoutUpdateView(UpdateView):
    model = Workout
    form_class = WorkoutForm
    template_name = 'workout/workout_form.html'
    success_url = reverse_lazy('workout_list')

class WorkoutDeleteView(DeleteView):
    model = Workout
    template_name = 'workout/workout_confirm_delete.html'
    success_url = reverse_lazy('workout_list')


class GoalCreateView(CreateView):
    model = Goal
    form_class = GoalForm
    template_name = 'goal/goal_form.html'
    success_url = reverse_lazy('goal_list')

class GoalListView(ListView):
    model = Goal
    template_name = 'goal/goal_list.html'

class GoalUpdateView(UpdateView):
    model = Goal
    form_class = GoalForm
    template_name = 'goal/goal_form.html'
    success_url = reverse_lazy('goal_list')

class GoalDeleteView(DeleteView):
    model = Goal
    template_name = 'goal/goal_confirm_delete.html'
    success_url = reverse_lazy('goal_list')



class ProgressCreateView(CreateView):
    model = Progress
    form_class = ProgressForm
    template_name = 'progress/progress_form.html'
    success_url = reverse_lazy('progress_list')

class ProgressListView(ListView):
    model = Progress
    template_name = 'progress/progress_list.html'

class ProgressUpdateView(UpdateView):
    model = Progress
    form_class = ProgressForm
    template_name = 'progress/progress_form.html'
    success_url = reverse_lazy('progress_list')

class ProgressDeleteView(DeleteView):
    model = Progress
    template_name = 'progress/progress_confirm_delete.html'
    success_url = reverse_lazy('progress_list')