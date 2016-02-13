from django.conf.urls import patterns, url
from video import views
#from djgeojson.views import GeoJSONLayerView

urlpatterns = [ 
	url(r'^$', views.index, name='videoIndex'),
	url(r'^init/$', views.init_content_caching, name='contentCaching'),
	url(r'^query/$', views.query, name='query'),
]
