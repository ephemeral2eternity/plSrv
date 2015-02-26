from django.conf.urls import patterns, url
from overlay import views
#from djgeojson.views import GeoJSONLayerView

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
	url(r'^query/$', views.query, name='query'),
	url(r'^edge/$', views.edge, name='edge'),
	url(r'^node/$', views.node, name='node'),
	url(r'^zone/$', views.zone, name='zone'),
)
