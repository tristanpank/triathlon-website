"""TriathlonWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views as api_views
from userAuth import views as auth_views

router = routers.DefaultRouter()
router.register(r'workouts', api_views.WorkoutEntryView, 'workouts')
router.register(r'register', auth_views.RegisterView, 'register')
# router.register(r'logout', auth_views.LogoutView, 'logout')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/login/', auth_views.LoginView.as_view(), name='login'),
    path('api/user/', auth_views.UserView.as_view(), name='user'),
    path('api/logout/', auth_views.User_logout, name='logout')
]
