from rest_framework import serializers
from .models import WorkoutEntry

class WorkoutEntrySerializer(serializers.ModelSerializer):
  class Meta:
    model = WorkoutEntry
    fields = ("id", "workout_type", "time_of_workout", "duration", "distance", "notes")
