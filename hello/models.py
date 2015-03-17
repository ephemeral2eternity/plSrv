from django.db import models
from decimal import Decimal
from djgeojson.fields import PointField
#from django.contrib.gis.db import models as gismodels

# Create your models here.
class PLCSite(models.Model):
	# site_id = models.IntegerField()
	site_name = models.CharField(max_length=200)
	site_url = models.CharField(max_length=1000)
	site_login_base = models.CharField(max_length=100)
	site_longitude = models.DecimalField(max_digits=10, decimal_places=5)
	site_latitude = models.DecimalField(max_digits=10, decimal_places=5)
	def __str__(self):
		return self.site_name

class PLCNode(models.Model):
	site_id = models.IntegerField()
	name = models.CharField(max_length=200)
	site = models.CharField(max_length=100, default="unknown")
	zone = models.CharField(max_length=100, default="unknown")
	region = models.CharField(max_length=100, default="unknown")
	node_type = models.CharField(max_length=200, default="unknown")
	node_ip = models.CharField(max_length=20, default="0.0.0.0")
	node_os = models.CharField(max_length=200, default="unknown")
	node_as = models.CharField(max_length=500, default="unknown")
	node_python = models.CharField(max_length=200, default="unknown")
	def __str__(self):
		return self.name

# Create GeoSite class to show site coordinates in a map
class GeoSite(models.Model):
	geom = PointField()
