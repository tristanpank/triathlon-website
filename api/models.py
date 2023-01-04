from django.db import models

# Create your models here.

class WorkoutEntry(models.Model):
  workout_type = models.CharField(max_length=30)
  time_of_workout = models.DateTimeField(auto_now_add=True)
  duration = models.DurationField()
  distance = models.IntegerField(default=0)
  notes = models.TextField()