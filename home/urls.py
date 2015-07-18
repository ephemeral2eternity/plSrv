from django.conf.urls import patterns, url
from hello import views
#from djgeojson.views import GeoJSONLayerView

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
)
