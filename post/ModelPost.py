# -*- encoding: utf-8 -*-
from post.models import Post
from comentarios.models import Comentario
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from django.db.models import Q

from categorias.models import Categoria
from etiquetas.models import Etiqueta
from comentarios.models import Comentario

from menu.models import Menu

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> V-A-L-I-D S-H-O-W P-O-S-T <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
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
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> V-A-L-I-D S-H-O-W P-O-S-T <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ITERACION FOR POST <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class QueryPostAddIteracion(object):
	def add(self,ObjPost,totalPost,page):
		paginator = Paginator(ObjPost,totalPost) # Mustra 7 post en el index
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
			file_info['image']=p.image
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

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ITERACION FOR POST <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

	
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> C-O-M-E-N-T-A-R-I-O-S <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
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
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> C-O-M-E-N-T-A-R-I-O-S <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> E-N-T-R-A-D-A-S <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class GetPostSlugMixin(ComentariosMixin):
	def GetPost(self,slug):
		ObjPost = Post.objects.get(slug=slug)
		idUser = self.request.user.id
		formatoMonth = "%b"

		PostMatriz = []
		p = ObjPost
		file_info = {}

		file_info['comentarios']= self.comenGet(p.id)

		file_info['id']=p.id
		file_info['title']=p.title
		file_info['image']=p.image
		file_info['slug']=p.slug
		file_info['descripcion']=p.descripcion
		file_info['first_name']=p.user.first_name
		file_info['last_name']=p.user.last_name
		file_info['fecha']=p.fecha_registro
		file_info['fecha_month']=p.fecha_registro.strftime(formatoMonth)
		file_info['categoria']=p.categoria
		ObjComentarioCount = Comentario.objects.filter(post__id=p.id,activo=True).count()
		file_info['comentariosCount']=ObjComentarioCount

		file_info['metadescripcion']=p.metadescripcion
		file_info['metakeywords']=p.metakeywords

		PostMatriz.append(file_info)
		return PostMatriz

class QueryPostMixin(QueryPostValid,QueryPostAddIteracion):
	def QueryPost(self,page,totalPost):

		ObjPost = self.all()# Mxin QueryPostValid

		PostMatriz = self.add(ObjPost,totalPost,page)# Mxin QueryPostAddIteracion

		return PostMatriz
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> E-N-T-R-A-D-A-S <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>B-U-S-Q-U-E-D-A <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<		
	def QueryPostBusqueda(self,page,query,totalPost):
		ObjPost = self.busqueda(query)# Mxin QueryPostValid

		PostMatriz = self.add(ObjPost,totalPost,page)# Mxin QueryPostAddIteracion
		return PostMatriz
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>B-U-S-Q-U-E-D-A <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<	

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> A-S-I-D-E <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class AsideMixin(object):
	def Etiquetas(self):
		EtiquetaMatriz = Etiqueta.objects.all()
		return EtiquetaMatriz
	
	def Categorias(self):
		ObjCategoria = Categoria.objects.all()
		return ObjCategoria

class AsidePostMixin(QueryPostValid,QueryPostAddIteracion):
	def QueryPostCategoria(self,page,cat,totalPost):
		ObjPost = self.categoria(cat)# Mxin QueryPostValid
		
		PostMatriz = self.add(ObjPost,totalPost,page)# Mxin QueryPostAddIteracion

	def QueryPostEtiquetas(self,page,tag,totalPost):
		ObjPost = self.etiqueta(tag)# Mxin QueryPostValid

		PostMatriz = self.add(ObjPost,totalPost,page)# Mxin QueryPostAddIteracion
		return PostMatriz	
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> A-S-I-D-E <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> M-E-N-U <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
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
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> M-E-N-U <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<		