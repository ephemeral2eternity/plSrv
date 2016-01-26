from django.conf.urls import patterns, url
from overlay import views
#from djgeojson.views import GeoJSONLayerView

urlpatterns = [ 
	url(r'^$', views.index, name='index'),
	url(r'^query/$', views.query, name='query'),
	url(r'^edge/$', views.edge, name='edge'),
	url(r'^node/$', views.node, name='node'),
	url(r'^zone/$', views.zone, name='zone'),
	url(r'^graph/$', views.graph, name='graph'),
	url(r'^overlay_json/$', views.overlay_json, name='overlay_json'),
]
