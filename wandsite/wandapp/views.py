from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer

from django.http import HttpResponse

# Create your views here.
def hello(request):
	return render(request, 'hello.html')

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer

def index(request):
	return HttpResponse("Hello, world. You're at the wandapp index.")