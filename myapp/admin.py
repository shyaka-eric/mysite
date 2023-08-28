from django.contrib import admin
from .models import Workout,Goal,Progress



admin.site.register(Workout)
admin.site.register(Goal)
admin.site.register(Progress)





class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'duration', 'intensity')
    search_fields = ('name', 'description')

class GoalAdmin(admin.ModelAdmin):
    list_display = ('user','target_date','goal_text','is_achieved')
    search_fields = ('user')

class ProgressAdmin(admin.ModelAdmin):
    list_display= ('user','date','weight','body_fat_percentage')

# Register your models here.