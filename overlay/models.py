from django.db import models

# Create your models here.
class Node(models.Model):
	name = models.CharField(max_length=10)
	ip = models.CharField(max_length=20)
	zone = models.CharField(max_length=20, default="")
	type = models.CharField(max_length=50, default="f1-micro")

class Edge(models.Model):
	src = models.CharField(max_length=10)
	dst = models.CharField(max_length=10)
