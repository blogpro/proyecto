from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import PostView

urlpatterns = patterns('',
    url(r'^post/$', PostView.as_view(), name='PostView'),
)
