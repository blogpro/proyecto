from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import User, Nota, NotaDetail

urlpatterns = patterns('',
   url(r'^user/$', User.as_view()),
   url(r'^nota/$', Nota.as_view()),
   url(r'^nota-detail/(?P<pk>[0-9]+)/$', NotaDetail.as_view()),

)
