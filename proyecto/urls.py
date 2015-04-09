from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyecto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('inicio.urls')),
    url(r'^',include('post.urls')),

    (r'^ckeditor/', include('ckeditor.urls')),

    url(r'^media/(?P<path>.*)$','django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT,}
    ),

    url(r'^static/(?P<path>.*)$','django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT_MOVIL,}
    ),


)
