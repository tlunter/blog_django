from django.conf.urls.defaults import *

urlpatterns = patterns('posts.views',
    url(r'^(?P<post_id>\d+)/$', 'show'),
    url(r'^(?P<post_id>\d+)/edit/$', 'edit'),
    url(r'^(?P<post_id>\d+)/delete/$', 'delete'),
    url(r'^new/$', 'new'),
    url(r'^$', 'index'),
)
