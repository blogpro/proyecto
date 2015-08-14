from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import AddImagenView, EditImegenPostView, DeleteImegnPostView

urlpatterns = patterns('',
#    url(r'^post/$', PostView.as_view(), name='PostView'),
	url(r'^add-imagen-post/(?P<pk>[0-9]+)/$', AddImagenView.as_view(), name='AddImagenView'),
	url(r'^edit-imagen-post/(?P<pk1>[0-9]+)/(?P<pk2>[0-9]+)/(?P<pk3>[0-9]+)/$', EditImegenPostView.as_view(), name='EditImegenPostView'),
    url(r'^delete-imagen-post/(?P<pk>[0-9]+)/$', DeleteImegnPostView.as_view(), name='DeleteImegnPostView'),
)
