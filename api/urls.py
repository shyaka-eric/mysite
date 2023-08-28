
from rest_framework.routers import DefaultRouter
#from .views import  WorkoutViewSet,GoalViewSet,ProgressViewSet
from .views import  WorkoutListCreateView, WorkoutRetrieveUpdateDeleteView
from .views import  GoalListCreateView, GoalRetrieveUpdateDeleteView
from .views import  ProgressListCreateView, ProgressRetrieveUpdateDeleteView
from django.urls import path, include
from . import views



urlpatterns= [

    path('workouts/',WorkoutListCreateView.as_view(),name='workout_list_api'),
    path('workouts/<int:pk>/',WorkoutRetrieveUpdateDeleteView.as_view(),name='Workout-detail'),
    path('goals/',GoalListCreateView.as_view(),name='goal_list_api'),
    path('goals/<int:pk>/',GoalRetrieveUpdateDeleteView.as_view(),name='goal-detail'),
    path('progresses/',ProgressListCreateView.as_view(),name='progress_list_api'),
    path('progresses/<int:pk>/',ProgressRetrieveUpdateDeleteView.as_view(),name='progress-detail'),


]