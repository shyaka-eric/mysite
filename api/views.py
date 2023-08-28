from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
#from rest_framework import viewsets
from myapp.models import Workout, Goal, Progress
from .serializers import WorkoutSerializer,GoalSerializer,ProgressSerializer
from rest_framework import permissions
from rest_framework.throttling import UserRateThrottle
from rest_framework.permissions import IsAuthenticated


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user == request.user


class WorkoutListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    queryset=Workout.objects.all()
    serializer_class=WorkoutSerializer
    
    

class WorkoutRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    queryset=Workout.objects.all()
    serializer_class=WorkoutSerializer
    
    


class GoalListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    queryset=Goal.objects.all()
    serializer_class=GoalSerializer
    
    permission_classes = [IsAuthenticated]

class GoalRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    queryset=Goal.objects.all()
    serializer_class=GoalSerializer
    
    
class ProgressListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    queryset=Progress.objects.all()
    serializer_class=ProgressSerializer
    
    

class ProgressRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    queryset=Progress.objects.all()
    serializer_class=ProgressSerializer
 
# Create your views here.
