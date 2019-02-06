from django.shortcuts import render

from rest_framework import viewsets,permissions
from .models import Movie
from .serializers import movieSerializer

# Create your views here.
class movieView(viewsets.ModelViewSet):
	queryset = Movie.objects.all()
	serializer_class = movieSerializer