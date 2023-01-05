from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):
  username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
  password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)

  class Meta:
    model = User
    fields = ('username', 'password', 'password2')
  
  def validate(self, attrs):
    if attrs['password'] != attrs['password2']:
      raise serializers.ValidationError({"password": "Password fields didn't match"})

    return attrs
  
  def create(self, validated_data):
    user = User.objects.create(
      username = validated_data['username']
    )

    user.set_password(validated_data['password'])
    user.save()

    return user

class LoginSerializer(serializers.Serializer):
  username = serializers.CharField(label="Username", write_only=True)
  password = serializers.CharField(label="Password", style={'input_type': 'password'}, trim_whitespace=False, write_only=True)

  def validate(self, attrs):
    username = attrs.get('username')
    password = attrs.get('password')

    if username and password:
      user = authenticate(request=self.context.get('request'), username=username, password=password)
    
      if not user:
        msg = "Access denied: wrong username and password"
        raise serializers.ValidationError(msg, code='authorization')
    
    else:
      msg = 'Both "username" and "password" are required'
      raise serializers.ValidationError(msg, code='authorization')
    
    attrs['user'] = user
    return attrs