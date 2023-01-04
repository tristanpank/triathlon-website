from django.contrib import admin
from .models import WorkoutEntry

# Register your models here.
class WorkoutEntryAdmin(admin.ModelAdmin):
  list_display = ('workout_type', 'time_of_workout', 'duration', 'distance', 'notes')

admin.site.register(WorkoutEntry, WorkoutEntryAdmin)