from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import PostView, UpdatePostViewPost, DetailPostViewPost, ListPostViewAngular, ListCategoriasView, ListEtiquetasView, ListComentariosViewAngular, ListStatusView

urlpatterns = patterns('',
    url(r'^new-post/$', PostView.as_view(), name='PostView'),
    url(r'^edit-post/(?P<pk>[0-9]+)/$', UpdatePostViewPost.as_view(), name='UpdatePostViewPost'),

    url(r'^blog/(?P<slug>[-\w]+)/$', DetailPostViewPost.as_view(), name='DetailPostViewPost'),

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>< A-N-G-U-L-A-R <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    url(r'^list-post-angular/$', ListPostViewAngular.as_view(), name='ListPostViewAngular'),#Angular
    url(r'^list-cat-angular/$', ListCategoriasView.as_view(), name='ListCategoriasView'),#Angular
    url(r'^list-tag-angular/$', ListEtiquetasView.as_view(), name='ListEtiquetasView'),#Angular
    url(r'^list-status-angular/$', ListStatusView.as_view(), name='ListStatusView'),#Angular

    url(r'^list-comentarios-angular/$', ListComentariosViewAngular.as_view(), name='ListComentariosViewAngular'),#Angular
)
