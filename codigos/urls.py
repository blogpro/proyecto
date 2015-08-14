from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import AddCodigoPostView, EditCodigoPostView, DeleteCodigoPostView

urlpatterns = patterns('',
#    url(r'^post/$', PostView.as_view(), name='PostView'),
	url(r'^add-codigo-post/(?P<pk>[0-9]+)/$', AddCodigoPostView.as_view(), name='AddCodigoPostView'),
	url(r'^edit-codigo-post/(?P<pk1>[0-9]+)/(?P<pk2>[0-9]+)/(?P<pk3>[0-9]+)/$', EditCodigoPostView.as_view(), name='EditCodigoPostView'),
    url(r'^delete-codigo-post/(?P<pk>[0-9]+)/$', DeleteCodigoPostView.as_view(), name='DeleteCodigoPostView'),
)
