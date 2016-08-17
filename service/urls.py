from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework.routers import DefaultRouter


from .views import ServicePostQuery, ServiceCategoriasQuery, ServiceEtiquetasQuery

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
)
