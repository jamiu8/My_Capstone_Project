from django.shortcuts import render
from rest_framework import generics
from .serializers import UserRegistrationSerializer
from django.contrib.auth import get_user_model

# Create your views here.


User = get_user_model()

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
