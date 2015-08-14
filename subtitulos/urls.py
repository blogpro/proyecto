from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import AddSubtituloPostView, EditSubtituloPostView, DeleteSubtituloPostView

urlpatterns = patterns('',
#    url(r'^post/$', PostView.as_view(), name='PostView'),
	url(r'^add-subtitulo-post/(?P<pk>[0-9]+)/$', AddSubtituloPostView.as_view(), name='AddSubtituloPostView'),
	url(r'^edit-subtitulo-post/(?P<pk1>[0-9]+)/(?P<pk2>[0-9]+)/(?P<pk3>[0-9]+)/$', EditSubtituloPostView.as_view(), name='EditSubtituloPostView'),
    url(r'^delete-subtitulo-post/(?P<pk>[0-9]+)/$', DeleteSubtituloPostView.as_view(), name='DeleteSubtituloPostView'),
)
