from django.conf.urls import *

urlpatterns = patterns('',
    url(r'^profile/$', 'auth.views.profile'),
    (r'^', include('django.contrib.auth.urls')),
)
