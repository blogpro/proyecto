from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import ServicePostQuery

urlpatterns = patterns('',
   url(r'^service-post-query/$', ServicePostQuery.as_view()),
   #url(r'^nota-detail/(?P<pk>[0-9º]+)/$', NotaDetail.as_view()),

)
