from django.conf.urls import patterns, url
from home import views
#from djgeojson.views import GeoJSONLayerView

urlpatterns = [ 
	url(r'^$', views.index, name='index'),
]
