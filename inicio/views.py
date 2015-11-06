# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404,render,redirect
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic import TemplateView, RedirectView, FormView, ListView

from menu.models import Menu
from categorias.models import Categoria
from etiquetas.models import Etiqueta

from django.contrib.auth import logout

from post.ModelPost import QueryPostMixin

def log_out(request):
    logout(request)
    return redirect('InicioViewInvitado')

# Create your views here.

def acceso_user(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook':
    	# for userg in user.group.all():
    	# 	print userg
        profile = user
        print profile
        #profile.gender = response.get('gender')


class MenuMixin(object):
	def Menus(self):
		#-------clases css del template para el diseño---
		ClassCssMenu = ['color1','color2','color3','color4','color5','color6']
		#-------clases css del template para el diseño---
		ObjMenu = Menu.objects.all()
		cont = 0
		MenuMatriz = []
		for M in ObjMenu:
			file_info = {}
			file_info['title_menu'] = M.descripcion
			file_info['css_menu'] = ClassCssMenu[cont]
			MenuMatriz.append(file_info)
			if cont != 5:
				cont = cont + 1
			else:
				cont = 0	
		return MenuMatriz
	

class AsideMixin(object):
	def Etiquetas(self):
		#-------clases css del template para el diseño---
		ClassCssEtiqueta = ['jol','lop','bun','live','dan','eva']
		#-------clases css del template para el diseño---
		ObjEtiqueta = Etiqueta.objects.all()
		cont = 0
		EtiquetaMatriz = []
		for E in ObjEtiqueta:
			file_info = {}
			file_info['title_etiqueta'] = E.title
			file_info['css_etiqueta'] = ClassCssEtiqueta[cont]
			EtiquetaMatriz.append(file_info)
			if cont != 5:
				cont = cont + 1
			else:
				cont = 0	
		return EtiquetaMatriz
	
	def Categorias(self):
		ObjCategoria = Categoria.objects.all()
		return ObjCategoria
			


class ValidaAccesoView(RedirectView):
	def get(self, args, **kwargs):
		if self.request.user.groups.filter(name='admin').exists():
			return redirect('InicioViewAdmin')
		if self.request.user.groups.filter(name='posteador').exists():
			return redirect('InicioViewAdmin')	
		else:
			return redirect('InicioViewInvitado')
		#return HttpResponseRedirect(url)


class InicioViewInvitado(MenuMixin,QueryPostMixin,AsideMixin,TemplateView):
    template_name = 'index.html'

    #Retorna los valores al template como nuevas variables
    def get_context_data(self, **kwargs):
		context = super(InicioViewInvitado, self).get_context_data(**kwargs)

		try:
			page = int(self.request.GET.get('page', '1'))
		except ValueError:
			page = 1

		ObjMenu = self.Menus()
		ObjEtiqueta = self.Etiquetas()
		ObjCategoria = self.Categorias()

		ObjQueryPost = self.QueryPost(page)

		data = {
			'Categoria':ObjCategoria,
			'Etiqueta':ObjEtiqueta,
			'Menu':ObjMenu,
			'PostMatriz':ObjQueryPost,
		}

		context.update(data)
		return context	


class InicioViewAdmin(MenuMixin,QueryPostMixin,AsideMixin,TemplateView):
    template_name = 'inicio_admin.html'

    #Retorna los valores al template como nuevas variables
    def get_context_data(self, **kwargs):
		context = super(InicioViewAdmin, self).get_context_data(**kwargs)

		try:
			page = int(self.request.GET.get('page', '1'))
		except ValueError:
			page = 1

		ObjMenu = self.Menus()
		ObjEtiqueta = self.Etiquetas()
		ObjCategoria = self.Categorias()

		ObjQueryPost = self.QueryPost(page)

		data = {
			'Categoria':ObjCategoria,
			'Etiqueta':ObjEtiqueta,
			'Menu':ObjMenu,
			'PostMatriz':ObjQueryPost,
		}

		context.update(data)
		return context



class Viewprueba(MenuMixin,QueryPostMixin,AsideMixin,TemplateView):
    template_name = 'pruebab.html'

    #Retorna los valores al template como nuevas variables
    def get_context_data(self, **kwargs):
		context = super(Viewprueba, self).get_context_data(**kwargs)

		try:
			page = int(self.request.GET.get('page', '1'))
		except ValueError:
			page = 1

		ObjMenu = self.Menus()
		ObjEtiqueta = self.Etiquetas()
		ObjCategoria = self.Categorias()

		ObjQueryPost = self.QueryPost(page)

		data = {
			'Categoria':ObjCategoria,
			'Etiqueta':ObjEtiqueta,
			'Menu':ObjMenu,
			'PostMatriz':ObjQueryPost,
		}

		context.update(data)
		return context			
