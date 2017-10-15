from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from project.api.serializers import UserSerializers

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user to be viewed or edited
    """
    queryset = User.objects.all()
    serializer_class = UserSerializers
