from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from rest_framework import generics, viewsets, views, permissions, status
from django.contrib.auth import login, logout
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class RegisterView(viewsets.ModelViewSet):
  queryset = User.objects.all()
  # permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer

class LoginView(views.APIView):
  permission_classes = (permissions.AllowAny,)

  def post(self, request, format=None):
    serializer = LoginSerializer(data=self.request.data, context={'request': self.request})
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    login(request, user)
    return Response(None, status=status.HTTP_202_ACCEPTED)

class UserView(generics.RetrieveAPIView):
  serializer_class = UserSerializer

  def get_object(self):
    return self.request.user

class LogoutView(viewsets.GenericViewSet):
  @action(methods=['POST', ], detail=False)
  def logout(self, request):
    logout(request)
    data = {'success': 'Succesfully logged out'}
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def User_logout(request):

    # request.user.auth_token.delete()

    logout(request)

    return Response('User Logged out successfully')