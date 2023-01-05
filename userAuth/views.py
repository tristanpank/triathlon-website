from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics, viewsets

# Create your views here.

class RegisterView(viewsets.ModelViewSet):
  queryset = User.objects.all()
  # permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer