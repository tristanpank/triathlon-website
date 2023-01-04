from django.shortcuts import render
from rest_framework import generics
from .serializers import WorkoutEntrySerializer
from .models import WorkoutEntry
# Create your views here.


class WorkoutEntryView(generics.ListCreateAPIView):
  queryset = WorkoutEntry.objects.all()
  serializer_class = WorkoutEntrySerializer