from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework.routers import DefaultRouter


from .views import ServicePostQuery, ServiceCategoriasQuery, ServiceEtiquetasQuery, ServiceComentariosQuery, ServiceImagenQuery

router = DefaultRouter()
#router.register(r'api', viewsetsCategoria)
#urlpatterns = router.urls

urlpatterns = patterns('',
	#Post
   	url(r'^service-post-query/$', ServicePostQuery.as_view()),
   	#Categorias
   	url(r'^service-categorias-query/$', ServiceCategoriasQuery.as_view()),
   	url(r'^service-categorias-query/(?P<pk>[0-9]+)/$', ServiceCategoriasQuery.as_view(), name='ServiceCategoriasQuery'),
   	#Etiquetas
   	url(r'^service-etiquetas-query/$', ServiceEtiquetasQuery.as_view()),
   	url(r'^service-etiquetas-query/(?P<pk>[0-9]+)/$', ServiceEtiquetasQuery.as_view(), name='ServiceEtiquetasQuery'),
   	#Comentarios
   	url(r'^service-comentarios-query/$', ServiceComentariosQuery.as_view()),
      url(r'^service-comentarios-query/(?P<pk>[0-9]+)/$', ServiceComentariosQuery.as_view(), name='ServiceComentariosQuery'),
      #Imagenes
      url(r'^service-imagen-query/$', ServiceImagenQuery.as_view()),
)
