from django.db import models

# Create your models here.
class CacheAgent(models.Model):
	# Client Name
	client = models.CharField(max_length=200)
	cache_agent = models.CharField(max_length=100)
	def __str__(self):
		return self.client
