from django.shortcuts import render
from django.http import HttpResponse
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets

# Create your views here.

def index (req):
    return HttpResponse("<h1>Hello World</h1>")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer