from rest_framework import serializers
from .models import Rating

class ratingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Rating
		fields = ('id','url','user', 'movie', 'rating','created_on')
