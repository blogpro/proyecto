from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import PostView, UpdatePostViewPost, DetailPostViewPost, AddItemPostView, EditItemPostView, DeleteItemPostView, ListPostViewAngular, ListCategoriasView, ListEtiquetasView, ListComentariosViewAngular

urlpatterns = patterns('',
    url(r'^new-post/$', PostView.as_view(), name='PostView'),
    url(r'^edit-post/(?P<pk>[0-9]+)/$', UpdatePostViewPost.as_view(), name='UpdatePostViewPost'),

    url(r'^blog/(?P<slug>[-\w]+)/$', DetailPostViewPost.as_view(), name='DetailPostViewPost'),

    url(r'^add-item-post/(?P<pk>[0-9]+)/$', AddItemPostView.as_view(), name='AddItemPostView'),
    url(r'^edit-item-post/(?P<pk1>[0-9]+)/(?P<pk2>[0-9]+)/$', EditItemPostView.as_view(), name='EditItemPostView'),
    url(r'^delete-item-post/(?P<pk1>[0-9]+)/(?P<pk2>[0-9]+)/$', DeleteItemPostView.as_view(), name='DeleteItemPostView'),

    url(r'^list-post-angular/$', ListPostViewAngular.as_view(), name='ListPostViewAngular'),#Angular
    url(r'^list-cat-angular/$', ListCategoriasView.as_view(), name='ListCategoriasView'),#Angular
    url(r'^list-tag-angular/$', ListEtiquetasView.as_view(), name='ListEtiquetasView'),#Angular

    url(r'^list-comentarios-angular/$', ListComentariosViewAngular.as_view(), name='ListComentariosViewAngular'),#Angular
)
