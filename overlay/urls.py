from django.conf.urls import patterns, url
from overlay import views
#from djgeojson.views import GeoJSONLayerView

urlpatterns = [ 
	url(r'^initManager/$', views.initManager, name='initManager'),
	url(r'^initNodes/$', views.initNodes, name='initNodes'),
	url(r'^initOverlay/$', views.initOverlay, name='initOverlay'),
	url(r'^queryOverlay/$', views.queryOverlay, name='queryOverlay'),
	url(r'^deleteOverlay/$', views.deleteOverlay, name='deleteOverlay'),
	url(r'^query/$', views.query, name='query'),
	url(r'^edge/$', views.get_edges, name='edge'),
	url(r'^node/$', views.get_nodes, name='node'),
	url(r'^overlaynode/$', views.get_overlay_nodes, name='overlaynode'),
	url(r'^zone/$', views.get_zones, name='zone'),
	url(r'^graph/$', views.graph, name='graph'),
	url(r'^add', views.add, name='add'),
	url(r'^overlay_json/$', views.overlay_json, name='overlay_json'),
]
