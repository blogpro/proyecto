from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import AddDescripcionPostView,EditDescripcionPostView,DeleteDescripcionPostView

urlpatterns = patterns('',
    #url(r'^new-post/$', PostView.as_view(), name='PostView'),
    url(r'^add-descripcion-post/(?P<pk>[0-9]+)/$', AddDescripcionPostView.as_view(), name='AddDescripcionPostView'),
    url(r'^edit-descripcion-post/(?P<pk1>[0-9]+)/(?P<pk2>[0-9]+)/(?P<pk3>[0-9]+)/$', EditDescripcionPostView.as_view(), name='EditDescripcionPostView'),
   url(r'^delete-item-post/(?P<pk>[0-9]+)/$', DeleteDescripcionPostView.as_view(), name='deletedescripcionpostView'),
)
