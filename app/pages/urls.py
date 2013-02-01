from django.conf.urls import *

urlpatterns = patterns('pages.views',
    url(r'^about/$', 'about'),
    url(r'^feeds/$', 'feeds'),
)
