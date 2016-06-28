# -*- encoding: utf-8 -*-
from post.models import Post,PostAdd
from comentarios.models import Comentario
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from categorias.models import Categoria
from etiquetas.models import Etiqueta

from menu.models import Menu

class AsideMixin(object):
	def Etiquetas(self):
		EtiquetaMatriz = Etiqueta.objects.all()
		return EtiquetaMatriz
	
	def Categorias(self):
		ObjCategoria = Categoria.objects.all()
		return ObjCategoria

class GetPostSlugMixin(object):
	def GetPost(self,slug):
		ObjPost = Post.objects.get(slug=slug)
		PostMatriz = []
		p = ObjPost
		file_info = {}

		#----------------------------------------Lista Post---------------------------------------
		ListaPost = []
		ObjPostAdd = PostAdd.objects.filter(post__id= p.id).order_by('order')
		for s in ObjPostAdd:
			file_info_html = {}
			if s.imagenpost != None:
				file_info_html['inicio_html']="<img class='img-responsive' src='"	
				file_info_html['codigo_pos'] =s.imagenpost
				file_info_html['fin_html']=" ' alt=''> "
				file_info_html['id_post_add']=s.id
			ListaPost.append(file_info_html)
		file_info['postList']=ListaPost
		#----------------------------------------Lista Post---------------------------------------

		file_info['title']=p.title
		file_info['slug']=p.slug
		file_info['descripcion']=p.descripcion
		file_info['first_name']=p.user.first_name
		file_info['last_name']=p.user.last_name
		file_info['fecha']=p.fecha_registro
		file_info['categoria']=p.categoria
		ObjComentarioCount = Comentario.objects.filter(post__id=p.id).count()
		file_info['comentarios']=ObjComentarioCount

		PostMatriz.append(file_info)
		return PostMatriz

class GetPostMixin(object):
	def GetPost(self,pk):
		ObjPost = Post.objects.get(pk=pk)
		PostMatriz = []
		p = ObjPost
		file_info = {}

		#----------------------------------------Lista Post---------------------------------------
		ListaPost = []
		ObjPostAdd = PostAdd.objects.filter(post__id= p.id).order_by('order')
		for s in ObjPostAdd:
			file_info_html = {}
			if s.imagenpost != None:
				file_info_html['inicio_html']="<img class='img-responsive' src='"	
				file_info_html['codigo_pos'] =s.imagenpost
				file_info_html['fin_html']=" ' alt=''> "
				file_info_html['id_post_add']=s.id
			ListaPost.append(file_info_html)
		file_info['postList']=ListaPost
		#----------------------------------------Lista Post---------------------------------------

		file_info['title']=p.title
		file_info['slug']=p.slug
		file_info['descripcion']=p.descripcion
		file_info['first_name']=p.user.first_name
		file_info['last_name']=p.user.last_name
		file_info['fecha']=p.fecha_registro
		file_info['categoria']=p.categoria
		ObjComentarioCount = Comentario.objects.filter(post__id=p.id).count()
		file_info['comentarios']=ObjComentarioCount

		PostMatriz.append(file_info)
		return PostMatriz	


class QueryPostMixin(object):
	def QueryPost(self,page):
		ObjPost = Post.objects.filter(status__id=1).order_by('-id')

		paginator = Paginator(ObjPost,7) # Mustra 7 post en el index
		try:
			contacts = paginator.page(page)
		except (EmptyPage, InvalidPage):
			contacts = paginator.page(paginator.num_pages)


		number_actual = int(contacts.number)
		number_previous = int(number_actual-1)
		number_next = int(number_actual+1)	

		ObjPost = contacts
		PostMatriz = []
		for p in ObjPost:
			file_info = {}

			#----------------------------------------Lista Post---------------------------------------
			ListaPost = []
			ObjPostAdd = PostAdd.objects.filter(post__id= p.id).order_by('order')
			for s in ObjPostAdd:
				file_info_html = {}
				if s.imagenpost != None:
					file_info_html['inicio_html']="<img class='img-responsive' src='"	
					file_info_html['codigo_pos'] =s.imagenpost
					file_info_html['fin_html']=" ' alt=''> "
					file_info_html['id_post_add']=s.id
				ListaPost.append(file_info_html)
			file_info['postList']=ListaPost
			#----------------------------------------Lista Post---------------------------------------

			
			file_info['previous_page_number'] = number_previous
			file_info['number'] = contacts.number
			file_info['num_pages'] = contacts.paginator.num_pages
			file_info['next_page_number'] = number_next

			file_info['title']=p.title
			file_info['slug']=p.slug
			file_info['descripcion']=p.descripcion
			file_info['id']=p.id
			file_info['first_name']=p.user.first_name
			file_info['last_name']=p.user.last_name
			file_info['fecha']=p.fecha_registro
			file_info['categoria']=p.categoria
			ObjComentarioCount = Comentario.objects.filter(post__id=p.id).count()
			file_info['comentarios']=ObjComentarioCount

			PostMatriz.append(file_info)
		return PostMatriz

class CategoriasPostMixin(object):
	def QueryPost(self,page,cat):
		ObjPost = Post.objects.filter(categoria__id=cat,status__id=1).order_by('-id')

		paginator = Paginator(ObjPost,7) # Mustra 7 post en el index
		try:
			contacts = paginator.page(page)
		except (EmptyPage, InvalidPage):
			contacts = paginator.page(paginator.num_pages)


		number_actual = int(contacts.number)
		number_previous = int(number_actual-1)
		number_next = int(number_actual+1)	

		ObjPost = contacts
		PostMatriz = []
		for p in ObjPost:
			file_info = {}

			#----------------------------------------Lista Post---------------------------------------
			ListaPost = []
			ObjPostAdd = PostAdd.objects.filter(post__id= p.id).order_by('order')
			for s in ObjPostAdd:
				file_info_html = {}
				if s.imagenpost != None:
					file_info_html['inicio_html']="<img class='img-responsive' src='"	
					file_info_html['codigo_pos'] =s.imagenpost
					file_info_html['fin_html']=" ' alt=''> "
					file_info_html['id_post_add']=s.id
				ListaPost.append(file_info_html)
			file_info['postList']=ListaPost
			#----------------------------------------Lista Post---------------------------------------

			
			file_info['previous_page_number'] = number_previous
			file_info['number'] = contacts.number
			file_info['num_pages'] = contacts.paginator.num_pages
			file_info['next_page_number'] = number_next

			file_info['title']=p.title
			file_info['slug']=p.slug
			file_info['descripcion']=p.descripcion
			file_info['id']=p.id
			file_info['first_name']=p.user.first_name
			file_info['last_name']=p.user.last_name
			file_info['fecha']=p.fecha_registro
			file_info['categoria']=p.categoria
			ObjComentarioCount = Comentario.objects.filter(post__id=p.id).count()
			file_info['comentarios']=ObjComentarioCount

			PostMatriz.append(file_info)
		return PostMatriz


class MenuMixin(object):
	def Menus(self):
		#-------clases css del template para el diseño---
		#ClassCssMenu = ['color1','color2','color3','color4','color5','color6']
		ClassCssMenu = ['color1','color1','color1','color1','color1','color1,','color1']
		#-------clases css del template para el diseño---
		ObjMenu = Menu.objects.all().order_by('order')
		cont = 0
		MenuMatriz = []
		for M in ObjMenu:
			file_info = {}
			file_info['title_menu'] = M.descripcion
			file_info['css_menu'] = ClassCssMenu[cont]
			file_info['slug'] = M.slug
			MenuMatriz.append(file_info)
			if cont != 5:
				cont = cont + 1
			else:
				cont = 0	
		return MenuMatriz