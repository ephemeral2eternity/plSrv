from django.conf.urls import patterns, url
from ping import views
#from djgeojson.views import GeoJSONLayerView

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^add/$', views.addRtts, name='add'),
]
