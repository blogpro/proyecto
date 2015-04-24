# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404,render
from django.template import RequestContext

from django.views.generic import TemplateView, RedirectView, FormView

from menu.models import Menu
from categorias.models import Categoria
from etiquetas.models import Etiqueta
from post.models import Post,PostAdd

from comentarios.models import Comentario

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
			



class InicioView(MenuMixin,AsideMixin,TemplateView):
    template_name = 'index.html'

    #Retorna los valores al template como nuevas variables
    def get_context_data(self, **kwargs):
		context = super(InicioView, self).get_context_data(**kwargs)
		ObjPost = Post.objects.all()

		ObjMenu = self.Menus()
		ObjEtiqueta = self.Etiquetas()
		ObjCategoria = self.Categorias()

		PostMatriz = []
		for p in ObjPost:
			file_info = {}

			#----------------------------------------Lista Post---------------------------------------
			ListaPost = []
			ObjPostAdd = PostAdd.objects.filter(post__id= p.id).order_by('order')
			for s in ObjPostAdd:
				file_info_html = {}
				if s.subtitulopost != None:
					file_info_html['inicio_html']="<br><h5>"
					file_info_html['codigo_pos'] = s.subtitulopost
					file_info_html['fin_html']="</br>"
				if s.descripcionpost != None:	
					file_info_html['inicio_html']="<p>"
					file_info_html['codigo_pos'] = s.descripcionpost
					file_info_html['fin_html']="</p>"
				if s.codigospost != None:	
					file_info_html['inicio_html']="<pre class='brush: python'>"
					file_info_html['codigo_pos'] = s.codigospost
					file_info_html['fin_html']="</pre>"
				if s.imagenpost != None:
					file_info_html['inicio_html']="<img class='img-responsive' src='"	
					file_info_html['codigo_pos'] =s.imagenpost
					file_info_html['fin_html']=" ' alt=''> "
				ListaPost.append(file_info_html)
			file_info['postList']=ListaPost
			#----------------------------------------Lista Post---------------------------------------

			
			file_info['title']=p.title
			file_info['first_name']=p.user.first_name
			file_info['last_name']=p.user.last_name
			file_info['fecha']=p.fecha_registro
			file_info['categoria']=p.categoria
			ObjComentarioCount = Comentario.objects.filter(post__id=p.id).count()
			file_info['comentarios']=ObjComentarioCount

			PostMatriz.append(file_info)

		data = {
			'Categoria':ObjCategoria,
			'Etiqueta':ObjEtiqueta,
			'Menu':ObjMenu,
			'Post':ObjPost,
			'PostMatriz':PostMatriz,
		}

		context.update(data)
		return context	

