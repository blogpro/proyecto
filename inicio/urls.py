from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import InicioView

urlpatterns = patterns('',
    url(r'^$', InicioView.as_view(), name='LoginView'),
)
