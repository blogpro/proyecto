# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404,render,redirect
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

#Seguridad para las vistas
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

from django.views.generic import TemplateView, RedirectView, FormView, ListView

from django.contrib.auth import logout

from post.ModelPost import MenuMixin, AsideMixin,  MenuMixin, QueryPostMixin, AsidePostMixin

class LoginRequiredInicio(object): 
	@method_decorator(permission_required('post.add_post'))
	def dispatch(self, request, *args, **kwargs): 
		return super(LoginRequiredInicio, self).dispatch(request, *args, **kwargs)

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

#Validacion por medio de la red social donde se realizo el login
class ValidaAccesoView(RedirectView):
	def get(self, args, **kwargs):
		if self.request.user.groups.filter(name='admin').exists():
			return redirect('InicioViewInvitado')
		if self.request.user.groups.filter(name='posteador').exists():
			return redirect('InicioViewInvitado')	
		else:
			return redirect('InicioViewInvitado')

class ValidaINicioView(RedirectView):
	def get(self, args, **kwargs):
		return redirect('InicioViewInvitado')

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<< Vistas principales <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class InicioViewInvitado(MenuMixin,QueryPostMixin,AsideMixin,TemplateView):
    template_name = 'index.html'

    #Retorna los valores al template como nuevas variables
    def get_context_data(self, **kwargs):
		context = super(InicioViewInvitado, self).get_context_data(**kwargs)

		ObjMenu = self.Menus()
		ObjEtiqueta = self.Etiquetas()
		ObjCategoria = self.Categorias()

		query = self.request.GET.get('s', '')
		if query:
			ObjQueryPost = self.QueryPostBusqueda(1,query,7)
		else:	
			ObjQueryPost = self.QueryPost(1,1)

		isPost = False;

		data = {
			'Categoria':ObjCategoria,
			'Etiqueta':ObjEtiqueta,
			'Menu':ObjMenu,
			'PostMatriz':ObjQueryPost,
			'isPost':isPost,
		}

		context.update(data)
		return context

class BlogViewInvitado(MenuMixin,QueryPostMixin,AsideMixin,TemplateView):
    template_name = 'index.html'

    #Retorna los valores al template como nuevas variables
    def get_context_data(self, **kwargs):
		context = super(BlogViewInvitado, self).get_context_data(**kwargs)

		try:
			page = int(self.request.GET.get('page', '1'))
		except ValueError:
			page = 1

		ObjMenu = self.Menus()
		ObjEtiqueta = self.Etiquetas()
		ObjCategoria = self.Categorias()

		query = self.request.GET.get('s', '')
		print query
		if query:
			ObjQueryPost = self.QueryPostBusqueda(page,query,7)
		else:	
			ObjQueryPost = self.QueryPost(page,7)

		isPost = True;
		data = {
			'Categoria':ObjCategoria,
			'Etiqueta':ObjEtiqueta,
			'Menu':ObjMenu,
			'PostMatriz':ObjQueryPost,
			'isPost':isPost,
		}

		context.update(data)
		return context

class PruebaViewInvitado(MenuMixin,QueryPostMixin,AsideMixin,TemplateView):
    template_name = 'index.html'
    #Retorna los valores al template como nuevas variables
    def get_context_data(self, **kwargs):
		context = super(PruebaViewInvitado, self).get_context_data(**kwargs)

		try:
			page = int(self.request.GET.get('page', '1'))
		except ValueError:
			page = 1

		ObjMenu = self.Menus()
		ObjEtiqueta = self.Etiquetas()
		ObjCategoria = self.Categorias()

		query = self.request.GET.get('s', '')
		if query:
			ObjQueryPost = self.QueryPostBusqueda(page,query,1)
		else:	
			ObjQueryPost = self.QueryPost(page,1)

		isPost = True;
		data = {
			'Categoria':ObjCategoria,
			'Etiqueta':ObjEtiqueta,
			'Menu':ObjMenu,
			'PostMatriz':ObjQueryPost,
			'isPost':isPost,
		}

		context.update(data)
		return context

class DashViewAdmin(LoginRequiredInicio,MenuMixin,QueryPostMixin,AsideMixin,TemplateView):
    template_name = 'indexDash.html'

    #Retorna los valores al template como nuevas variables
    def get_context_data(self, **kwargs):
		context = super(DashViewAdmin, self).get_context_data(**kwargs)

		try:
			page = int(self.request.GET.get('page', '1'))
		except ValueError:
			page = 1

		ObjMenu = self.Menus()
		ObjEtiqueta = self.Etiquetas()
		ObjCategoria = self.Categorias()

		#-------------Lista de post QueryPostMixin----------
		ObjQueryPost = self.QueryPost(page)
		#-------------Lista de post QueryPostMixin----------

		isPost = True;

		data = {
			'Categoria':ObjCategoria,
			'Etiqueta':ObjEtiqueta,
			'Menu':ObjMenu,
			'PostMatriz':ObjQueryPost,
			'isPost':isPost,
		}

		context.update(data)
		return context

class BaseDashViewAngular(LoginRequiredInicio,TemplateView):
	template_name = 'baseDashAngular.html'

class indexViewDashAngular(LoginRequiredInicio,TemplateView):
	template_name = 'indexDash.html'					
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<< Vistas principales <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#>************************************* vista para mostrar los post por categorias ******************************≤
class CategoriaQueryPost(MenuMixin,AsidePostMixin,AsideMixin,TemplateView):
    template_name = 'index.html'

    #Retorna los valores al template como nuevas variables
    def get_context_data(self, **kwargs):
		context = super(CategoriaQueryPost, self).get_context_data(**kwargs)

		try:
			page = int(self.request.GET.get('page', '1'))
		except ValueError:
			page = 1

		ObjMenu = self.Menus()
		ObjEtiqueta = self.Etiquetas()
		ObjCategoria = self.Categorias()

		idCategoria = self.kwargs['pk']

		ObjQueryPost = self.QueryPostCategoria(page,idCategoria,7)

		isPost = True;
		data = {
			'Categoria':ObjCategoria,
			'Etiqueta':ObjEtiqueta,
			'Menu':ObjMenu,
			'PostMatriz':ObjQueryPost,
			'isPost':isPost,
		}

		context.update(data)
		return context

class EtiquetasQueryPost(MenuMixin,AsidePostMixin,AsideMixin,TemplateView):
    template_name = 'index.html'

    #Retorna los valores al template como nuevas variables
    def get_context_data(self, **kwargs):
		context = super(EtiquetasQueryPost, self).get_context_data(**kwargs)

		try:
			page = int(self.request.GET.get('page', '1'))
		except ValueError:
			page = 1

		ObjMenu = self.Menus()
		ObjEtiqueta = self.Etiquetas()
		ObjCategoria = self.Categorias()

		idEtiquetas = self.kwargs['pk']

		ObjQueryPost = self.QueryPostEtiquetas(page,idEtiquetas,7)
		isPost = True;
		data = {
			'Categoria':ObjCategoria,
			'Etiqueta':ObjEtiqueta,
			'Menu':ObjMenu,
			'PostMatriz':ObjQueryPost,
			'isPost':isPost,
		}

		context.update(data)
		return context		
#>************************************* vista para mostrar los post por categorias ******************************≤