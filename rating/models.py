from django.db import models
from django.conf import settings
from movies.models import Movie

class Rating(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie')
	rating = models.IntegerField(default=0)
	created_on = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return str(self.id)+'--'+str(self.movie.title)+'--'+ str(self.user.username)