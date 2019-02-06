from rest_framework import serializers
from .models import Movie

class movieSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Movie
		fields = ('id','url','title', 'imdbId', 'about','movieImage', 'yearOfRelease','created_on')