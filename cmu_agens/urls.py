from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cmu_agens.views.home', name='home'),
    url(r'^hello/', include('hello.urls', namespace='hello')),
    url(r'^overlay/', include('overlay.urls', namespace='overlay')),
    url(r'^ping/', include('ping.urls', namespace='ping')),
    url(r'^admin/', include(admin.site.urls)),
)
