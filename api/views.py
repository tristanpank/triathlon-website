from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializers import WorkoutEntrySerializer
from .models import WorkoutEntry
# Create your views here.


class WorkoutEntryView(viewsets.ModelViewSet):
  queryset = WorkoutEntry.objects.all()
  serializer_class = WorkoutEntrySerializer