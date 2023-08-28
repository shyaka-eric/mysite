from django.urls import path
from django.urls import path, include
from . import views
from .views import (
    WorkoutCreateView,
    WorkoutListView,
    WorkoutUpdateView,
    WorkoutDeleteView,
    GoalCreateView,
    GoalListView,
    GoalUpdateView,
    GoalDeleteView, 
    ProgressCreateView,
    ProgressListView,
    ProgressUpdateView,
    ProgressDeleteView,
    
    )



urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    
    path('workout/create/', WorkoutCreateView.as_view(), name='workout_create'),
    path('workouts/', WorkoutListView.as_view(), name='workout_list'),
    path('workout/<int:pk>/update/', WorkoutUpdateView.as_view(), name='workout_update'),
    path('workout/<int:pk>/delete/', WorkoutDeleteView.as_view(), name='workout_delete'),
    
    path('goal/create/', GoalCreateView.as_view(), name='goal_create'),
    path('goals/', GoalListView.as_view(), name='goal_list'),
    path('goal/<int:pk>/update/', GoalUpdateView.as_view(), name='goal_update'),
    path('goal/<int:pk>/delete/', GoalDeleteView.as_view(), name='goal_delete'),

    path('progress/create/', ProgressCreateView.as_view(), name='progress_create'),
    path('progress/', ProgressListView.as_view(), name='progress_list'),
    path('progress/<int:pk>/update/', ProgressUpdateView.as_view(), name='progress_update'),
    path('progress/<int:pk>/delete/', ProgressDeleteView.as_view(), name='progress_delete'),
    
]
