from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import ValidaAccesoView, InicioViewInvitado, DashViewAdmin,ValidaINicioView, CategoriaQueryPost, EtiquetasQueryPost

urlpatterns = patterns('',
	url(r'^validar-acceso/$', ValidaAccesoView.as_view(), name='validaAcceso'),

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Url para el acceso <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    url(r'^$', InicioViewInvitado.as_view(), name='InicioViewInvitado'),#Invitado
    url(r'^dash-admin/$', DashViewAdmin.as_view(), name='DashViewAdmin'),#Admin
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Url para el acceso <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



    url(r'^log-out/$', 'inicio.views.log_out', name='log-out'),
    url(r'^inicio/$', ValidaINicioView.as_view(), name='ValidaINicioView'),
    
    #QUERY POST BY ASIDE
    url(r'^categorias/(?P<pk>[0-9]+)/$', CategoriaQueryPost.as_view(), name='CategoriaQueryPost'),
    url(r'^etiquetas/(?P<pk>[0-9]+)/$', EtiquetasQueryPost.as_view(), name='EtiquetasQueryPost'),
)
