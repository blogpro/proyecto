# -*- encoding: utf-8 -*-
from post.models import Post,PostAdd
from comentarios.models import Comentario
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from django.db.models import Q

from categorias.models import Categoria
from etiquetas.models import Etiqueta
from comentarios.models import Comentario

from menu.models import Menu

class QueryPostValid(object):
	def all(self):
		user = self.request.user
		if user.groups.filter(name='Administrador').exists():
			ObjPost = Post.objects.all().exclude(status__in=[5]).order_by('-id')
		else:
			ObjPost = Post.objects.filter(status__id=1).order_by('-id')
		return ObjPost	
	def busqueda(self,query):
		user = self.request.user
		if user.groups.filter(name='Administrador').exists():
			ObjPost = Post.objects.filter(Q(title__icontains=query) | Q(descripcion__icontains=query)).exclude(status__in=[5]).order_by('-id')
		else:
			ObjPost = Post.objects.filter(status__id=1).filter(Q(title__icontains=query) | Q(descripcion__icontains=query)).order_by('-id')
		return ObjPost	
	def categoria(self,cat):
		user = self.request.user
		if user.groups.filter(name='Administrador').exists():
			ObjPost = Post.objects.filter(categoria__id=cat).exclude(status__in=[5]).order_by('-id')
		else:
			ObjPost = Post.objects.filter(categoria__id=cat,status__id=1).order_by('-id')
		return ObjPost	
	def etiqueta(self,tag):
		user = self.request.user
		if user.groups.filter(name='Administrador').exists():
			ObjPost = Post.objects.filter(etiquetas__in=tag).exclude(status__in=[5]).order_by('-id')
		else:
			ObjPost = Post.objects.filter(etiquetas__in=tag,status__id=1).order_by('-id')
		return ObjPost	

		
	

class ComentariosMixin(object):
	def comenGet(self,idpost):
		idUser = self.request.user.id
		ListaCommen = []
		ObjModelComen = Comentario.objects.filter(post__id=idpost).order_by('-id')
		formatoF= "%d %B %Y"  # Asigna un formato de ejemplo1
		formatoH = "%I:%M:%S %p"  # Asigna un formato de ejemplo1
		for c in ObjModelComen:
			file_info_html = {}
			if c.activo == True or c.user.id == idUser:
				file_info_html['id'] =c.id
				file_info_html['descripcion'] =c.descripcion
				file_info_html['first_name'] =c.user.first_name
				file_info_html['last_name'] =c.user.last_name
				file_info_html['fecha_hora'] = c.fechahora
				file_info_html['fechaJs'] = c.fechahora.strftime(formatoF)
				file_info_html['horaJs'] = c.fechahora.strftime(formatoH)
				file_info_html['activo'] = c.activo
				if c.activo == False:
					file_info_html['nota'] = u'Comentario en proceso de validación. Solo es visible para ti.'
				ListaCommen.append(file_info_html)
		return ListaCommen	

class AsideMixin(object):
	def Etiquetas(self):
		EtiquetaMatriz = Etiqueta.objects.all()
		return EtiquetaMatriz
	
	def Categorias(self):
		ObjCategoria = Categoria.objects.all()
		return ObjCategoria

class GetPostSlugMixin(ComentariosMixin):
	def GetPost(self,slug):
		ObjPost = Post.objects.get(slug=slug)
		idUser = self.request.user.id
		PostMatriz = []
		p = ObjPost
		file_info = {}

		file_info['comentarios']= self.comenGet(p.id)

		file_info['id']=p.id
		file_info['title']=p.title
		file_info['slug']=p.slug
		file_info['descripcion']=p.descripcion
		file_info['first_name']=p.user.first_name
		file_info['last_name']=p.user.last_name
		file_info['fecha']=p.fecha_registro
		file_info['categoria']=p.categoria
		ObjComentarioCount = Comentario.objects.filter(post__id=p.id,activo=True).count()
		file_info['comentariosCount']=ObjComentarioCount

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
		ObjComentarioCount = Comentario.objects.filter(post__id=p.id,activo=True).count()
		file_info['comentariosCount']=ObjComentarioCount

		PostMatriz.append(file_info)
		return PostMatriz	


class QueryPostMixin(QueryPostValid):
	def QueryPost(self,page):

		ObjPost = self.all()# Mxin QueryPostValid

		paginator = Paginator(ObjPost,7) # Mustra 7 post en el index
		try:
			contacts = paginator.page(page)
		except (EmptyPage, InvalidPage):
			contacts = paginator.page(paginator.num_pages)


		number_actual = int(contacts.number)
		number_previous = int(number_actual-1)
		number_next = int(number_actual+1)

		formatoMonth = "%b"

		ObjPost = contacts
		PostMatriz = []
		for p in ObjPost:
			file_info = {}
			
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
			file_info['fecha_month']=p.fecha_registro.strftime(formatoMonth)
			file_info['categoria']=p.categoria
			ObjComentarioCount = Comentario.objects.filter(post__id=p.id,activo=True).count()
			file_info['comentariosCount']=ObjComentarioCount

			PostMatriz.append(file_info)
		return PostMatriz
	def QueryPostBusqueda(self,page,query):
		ObjPost = self.busqueda(query)# Mxin QueryPostValid

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
			file_info['comentariosCount']=ObjComentarioCount

			PostMatriz.append(file_info)
		return PostMatriz	

class AsidePostMixin(QueryPostValid):
	def QueryPostCategoria(self,page,cat):
		ObjPost = self.categoria(cat)# Mxin QueryPostValid
		
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
			file_info['comentariosCount']=ObjComentarioCount

			PostMatriz.append(file_info)
		return PostMatriz

	def QueryPostEtiquetas(self,page,tag):
		ObjPost = self.etiqueta(tag)# Mxin QueryPostValid

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
			file_info['comentariosCount']=ObjComentarioCount

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