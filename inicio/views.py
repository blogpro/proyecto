# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404,render
from django.template import RequestContext

from django.views.generic import TemplateView, RedirectView, FormView

from menu.models import Menu
from categorias.models import Categoria
from etiquetas.models import Etiqueta



from post.ModelPost import QueryPostMixin

# Create your views here.

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
			



class InicioView(MenuMixin,QueryPostMixin,AsideMixin,TemplateView):
    template_name = 'index.html'

    #Retorna los valores al template como nuevas variables
    def get_context_data(self, **kwargs):
		context = super(InicioView, self).get_context_data(**kwargs)

		ObjMenu = self.Menus()
		ObjEtiqueta = self.Etiquetas()
		ObjCategoria = self.Categorias()

		ObjQueryPost = self.QueryPost()

		data = {
			'Categoria':ObjCategoria,
			'Etiqueta':ObjEtiqueta,
			'Menu':ObjMenu,
			'PostMatriz':ObjQueryPost,
		}

		context.update(data)
		return context	

