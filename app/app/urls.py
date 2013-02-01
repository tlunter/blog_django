from django.conf.urls import *

urlpatterns = patterns('',
    (r'^posts/', include('posts.urls')),
    (r'^pages/', include('pages.urls')),
    (r'^comments/', include('comments.urls')),
    (r'^accounts/', include('auth.urls')),
    url(r'^$', 'posts.views.index'),
)
