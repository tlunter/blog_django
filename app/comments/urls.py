from django.conf.urls.defaults import *

urlpatterns = patterns('comments.views',
    url(r'^(?P<comment_id>\d+)/$', 'show'),
    url(r'^(?P<comment_id>\d+)/edit/$', 'edit'),
    url(r'^(?P<comment_id>\d+)/delete/$', 'delete'),
    url(r'^(?P<post_id>\d+)/new/$', 'new'),
    url(r'^user/(?P<user_id>\d+)/$', 'index'),
)
