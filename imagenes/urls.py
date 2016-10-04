from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import DeleteImegnPostView

urlpatterns = patterns('',
#    url(r'^post/$', PostView.as_view(), name='PostView'),
    url(r'^delete-imagen-post/(?P<pk>[0-9]+)/$', DeleteImegnPostView.as_view(), name='DeleteImegnPostView'),
)
