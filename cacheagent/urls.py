from django.conf.urls import patterns, url
from cacheagent import views
#from djgeojson.views import GeoJSONLayerView

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
	url(r'^add$', views.add, name='add'),
	url(r'^dump/$', views.dump, name='dump'),
	url(r'^delete/$', views.delete, name='delete'),
)
