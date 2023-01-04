from django.urls import path
from . import views


urlpatterns = [
    path('', views.WorkoutEntryView.as_view())
]
