from django.conf.urls import patterns, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'Easter.views.index'),
    url(r'^post/$', 'Easter.views.index'),
    url(r'^update/(?P<field>.+)/(?P<id>\d+)/?$', 'Easter.views.update'),
    url(r'^admin/', (admin.site.urls)),
)
