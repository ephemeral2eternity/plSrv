from django.conf.urls import patterns, url
from overlay import views
#from djgeojson.views import GeoJSONLayerView

urlpatterns = [ 
	url(r'^initNodes/$', views.initNodes, name='initNodes'),
	url(r'^initEdges/$', views.initEdges, name='initEdges'),
	url(r'^query/$', views.query, name='query'),
	url(r'^edge/$', views.get_edges, name='edge'),
	url(r'^node/$', views.get_nodes, name='node'),
	url(r'^zone/$', views.get_zones, name='zone'),
	url(r'^graph/$', views.graph, name='graph'),
	url(r'^overlay_json/$', views.overlay_json, name='overlay_json'),
]
