from django.shortcuts import render

from rest_framework import viewsets,permissions
from .models import User
from .serializers import userSerializer

# Create your views here.
class userView(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = userSerializer