from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import ValidaAccesoView, InicioViewInvitado, BlogViewInvitado, DashViewAdmin,ValidaINicioView, CategoriaQueryPost, EtiquetasQueryPost, BaseDashViewAngular, indexViewDashAngular, PruebaViewInvitado

urlpatterns = patterns('',
	url(r'^validar-acceso/$', ValidaAccesoView.as_view(), name='validaAcceso'),

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Url para el acceso <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    url(r'^$', InicioViewInvitado.as_view(), name='InicioViewInvitado'),#Invitado
    url(r'^blog/$', BlogViewInvitado.as_view(), name='BlogViewInvitado'),#Invitado

    url(r'^prueba/$', PruebaViewInvitado.as_view(), name='PruebaViewInvitado'),#Invitado

    url(r'^dash-admin/$', BaseDashViewAngular.as_view(), name='BaseDashViewAngular'),#Admin Angular
    url(r'^index-dash-post-angular/$', indexViewDashAngular.as_view(), name='indexViewDashAngular'),#Admin Angular
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Url para el acceso <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    url(r'^log-out/$', 'inicio.views.log_out', name='log-out'),
    url(r'^inicio/$', ValidaINicioView.as_view(), name='ValidaINicioView'),
    
    #QUERY POST BY ASIDE
    url(r'^blog/categorias/(?P<pk>[0-9]+)/$', CategoriaQueryPost.as_view(), name='CategoriaQueryPost'),
    url(r'^blog/etiquetas/(?P<pk>[0-9]+)/$', EtiquetasQueryPost.as_view(), name='EtiquetasQueryPost'),

 
)
