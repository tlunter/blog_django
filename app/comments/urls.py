from django.conf.urls.defaults import *

urlpatterns = patterns('comments.views',
    url(r'^(?P<comment_id>\d+)/$', 'show'),
    url(r'^user/(?P<user_id>\d+)/$', 'index'),
)
