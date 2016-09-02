from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from django.http import HttpResponse

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyecto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #----------------google--------------------
    (r'^google0aaeb5398aea27d9\.html$', lambda r: HttpResponse("google-site-verification: google0aaeb5398aea27d9.html")),
    (r'^sitemap\.xml$', lambda r: HttpResponse("google-site-verification: sitemap.xml")),
    #----------------google--------------------

    url(r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name': 'admin/login.html'}),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('inicio.urls')),
    url(r'^',include('post.urls')),
    #url(r'^',include('comentarios.urls')),
    #url(r'^',include('subtitulos.urls')),
    #url(r'^',include('codigos.urls')),
    url(r'^',include('imagenes.urls')),
    url(r'^',include('service.urls')),

    url('', include('social.apps.django_app.urls', namespace='social')),

    (r'^/ckeditor/', include('ckeditor.urls')),

    url(r'^media/(?P<path>.*)$','django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT,}
    ),

    url(r'^static/(?P<path>.*)$','django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT_MOVIL,}
    ),


)
