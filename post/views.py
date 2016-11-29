# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404,render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, RedirectView, FormView, DetailView, UpdateView

#Seguridad para las vistas
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator




from menu.models import Menu
from categorias.models import Categoria
from etiquetas.models import Etiqueta
from post.models import Post

from comentarios.models import Comentario


from .form import PostForm
from comentarios.form import ComentarioForm

from .ModelPost import MenuMixin, AsideMixin, GetPostSlugMixin, QueryPostMixin
from django.core.urlresolvers import reverse

class LoginRequiredMixin(object): 
	@method_decorator(permission_required('post.add_post'))
	def dispatch(self, request, *args, **kwargs): 
		return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


# Create your views here.
class PostView(LoginRequiredMixin,FormView):
    template_name = 'dashpost.html'
    form_class = PostForm
    #success_url = '/add-item-post/'

    def form_valid(self, form):

        new_post=form.save(commit=False)
        new_post.user = self.request.user
        new_post.save()


        return HttpResponseRedirect("/dash-admin/#/list-post/")
    def form_invalid(self, form):
    	return self.render_to_response(self.get_context_data(form=form))    
    
    

    #Retorna los valores al template como nuevas variables
    def get_context_data(self, **kwargs):
		context = super(PostView, self).get_context_data(**kwargs)
		ObjPost = Post.objects.all().order_by('-id')[:1]
		ObjFormPost = PostForm()

		data = {
			'ObjFormPost':ObjFormPost,
			'Post':ObjPost,
		}

		context.update(data)
		return context

class UpdatePostViewPost(LoginRequiredMixin,UpdateView):

	template_name = 'dashpost.html'
	model = Post
	form_class=PostForm
	fields = ['status', 'title','etiquetas','categoria','descripcion','image']

	success_url = '/dash-admin/#/list-post/'
	
	def get_context_data(self, **kwargs):

		context = super(UpdatePostViewPost, self).get_context_data(**kwargs)
		context['ObjFormPost'] = reverse('UpdatePostViewPost',kwargs={'pk': self.get_object().id})

		return context

class DetailPostViewPost(MenuMixin,AsideMixin,GetPostSlugMixin, DetailView):
	model = Post
	template_name = 'ver-mas-post-prueba.html'

	#Retorna los valores al template como nuevas variables
	def get_context_data(self, **kwargs):
		context = super(DetailPostViewPost, self).get_context_data(**kwargs)

		ObjMenu = self.Menus()
		ObjEtiqueta = self.Etiquetas()
		ObjCategoria = self.Categorias()

		id_post = self.kwargs['slug']

		ObjGetPost = self.GetPost(id_post)
		#ObjPostAdd = PostAdd.objects.filter(post__id=id_post)

		data = {
			'Categoria':ObjCategoria,
			'Etiqueta':ObjEtiqueta,
			'Menu':ObjMenu,
			'PostMatriz':ObjGetPost,
			'id_post':id_post
		}

		context.update(data)
		return context

# <<<<<<<<<<<<<<<<<<< Viws Angular >>>>>>>>>>>>>>>>>>>>>>>
class ListPostViewAngular(LoginRequiredMixin,TemplateView):
	template_name = 'dashlistpost.html'
class ListCategoriasView(LoginRequiredMixin,TemplateView):
	template_name = 'dashcategoriapost.html'
class ListEtiquetasView(LoginRequiredMixin,TemplateView):
	template_name = 'dashetiquetaspost.html'
class ListStatusView(LoginRequiredMixin,TemplateView):
	template_name = 'dashstatuspost.html'	
class ListComentariosViewAngular(LoginRequiredMixin,TemplateView):
	template_name = 'dashlistcommen.html'
# <<<<<<<<<<<<<<<<<<< Viws Angular >>>>>>>>>>>>>>>>>>>>>>>	