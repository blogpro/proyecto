from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import ValidaAccesoView, InicioViewInvitado, InicioViewAdmin

urlpatterns = patterns('',
	url(r'^validar-acceso/$', ValidaAccesoView.as_view(), name='validaAcceso'),

    url(r'^$', InicioViewInvitado.as_view(), name='InicioViewInvitado'),#Invitado

    url(r'^access-admin-site/$', InicioViewAdmin.as_view(), name='InicioViewAdmin'),#Admin


    url(r'^log-out/$', 'inicio.views.log_out', name='log-out'),
)
