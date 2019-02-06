from django.db import models
from django.conf import settings
from datetime import datetime
def image_upload_path(instance, filename):
	return "Movie/{0}".format(instance.imdbId, filename)

class Movie(models.Model):
	# Title, imdbId, YearOfRelease,image,about
	title = models.CharField(max_length=250, null=True, blank=True)
	imdbId = models.CharField(max_length=50, null=True, blank=True)
	about = models.TextField(null=True)
	movieImage = models.CharField(max_length=900, null=True, blank=True)
	yearOfRelease = models.DateField(blank=True)
	created_on = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return str(self.id)+'--'+ str(self.title)