from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', include('home.urls'), name='home'),
    url(r'^hello/', include('hello.urls', namespace='hello')),
    url(r'^overlay/', include('overlay.urls', namespace='overlay')),
    url(r'^ping/', include('ping.urls', namespace='ping')),
    url(r'^cacheagent/', include('cacheagent.urls', namespace='cacheagent')),
    url(r'^admin/', include(admin.site.urls)),
)
