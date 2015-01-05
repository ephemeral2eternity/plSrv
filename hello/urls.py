from django.conf.urls import patterns, url
from hello import views
#from djgeojson.views import GeoJSONLayerView

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
	url(r'^site/$', views.addsite, name='sites'),
	url(r'^node/$', views.addnode, name='nodes'),
	url(r'^map/$', views.map, name='map'),
	url(r'^site/(?P<site_id>\d+)/$', views.site_detail, name='site_detail'),
	url(r'^node/(?P<node_id>\d+)/$', views.node_detail, name='node_detail'),
	#url(r'^data.geojson$', GeoJSONLayerView.as_view(model=MushroomSpot), name='data'),
)
