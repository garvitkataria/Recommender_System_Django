from rest_framework import serializers
from .models import User

class userSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('id','url',  'username', 'email', 'password', 'mobile_no','recomended')
