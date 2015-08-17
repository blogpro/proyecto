from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import InicioView, InicioViewAdmin

urlpatterns = patterns('',
    url(r'^$', InicioView.as_view(), name='LoginView'),
    url(r'^access-admin-site/$', InicioViewAdmin.as_view(), name='InicioViewAdmin'),

    url(r'^log-out/$', 'inicio.views.log_out', name='log-out'),
)
