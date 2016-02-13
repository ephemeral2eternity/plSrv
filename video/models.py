from django.db import models

# Create your models here.
class Cache(models.Model):
	server = models.CharField(max_length=20)
	videos = models.CharField(max_length=5000)
	def __str__(self):
		return self.name
