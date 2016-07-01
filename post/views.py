# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404,render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, RedirectView, FormView, DetailView, UpdateView

#Seguridad para las vistas
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator




from menu.models import Menu
from categorias.models import Categoria
from etiquetas.models import Etiqueta
from post.models import Post,PostAdd

from comentarios.models import Comentario


from .form import PostForm

from .ModelPost import MenuMixin, AsideMixin, GetPostMixin, GetPostSlugMixin, QueryPostMixin
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

        idn = str(new_post.id)
        return HttpResponseRedirect("/add-item-post/"+idn+"/")
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

class UpdatePostViewPost(UpdateView):

	form_class=PostForm
	model = Post
	template_name = 'dashpost.html'

	def get_context_data(self, **kwargs):

		context = super(UpdatePostViewPost, self).get_context_data(**kwargs)
		context['ObjFormPost'] = reverse('UpdatePostViewPost',kwargs={'pk': self.get_object().id})

		return context

class DetailPostViewPost(MenuMixin,AsideMixin,GetPostSlugMixin, DetailView):
	model = Post
	template_name = 'detailpost.html'
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
			#'ObjPostAdd':ObjPostAdd,
			'id_post':id_post,
		}

		context.update(data)
		return context



class AddItemPostView(LoginRequiredMixin,GetPostMixin,TemplateView):
    template_name = 'dashAddItemPost.html'
      
    #Retorna los valores al template como nuevas variables
    def get_context_data(self, **kwargs):
		context = super(AddItemPostView, self).get_context_data(**kwargs)
		ObjMenu = Menu.objects.all()

		id_post = self.kwargs['pk']

		ObjGetPost = self.GetPost(id_post)
		ObjPostAdd = PostAdd.objects.filter(post__id=id_post)

		data = {
			'Menu':ObjMenu,
			'PostMatriz':ObjGetPost,
			'ObjPostAdd':ObjPostAdd,
			'id_post':id_post,
		}

		context.update(data)
		return context



class EditItemPostView(RedirectView):

	def get(self, args, **kwargs):
		post_id = self.kwargs.get('pk1', None)
		postitem_id = self.kwargs.get('pk2', None)

		ObjPostAdd = get_object_or_404(PostAdd, pk=postitem_id)

		v_subtitulopost = ObjPostAdd.subtitulopost
		v_descripcionpost = ObjPostAdd.descripcionpost
		v_codigospost = ObjPostAdd.codigospost
		v_imagenpost = ObjPostAdd.imagenpost



		if v_subtitulopost != None:
			url = "/edit-subtitulo-post/"
			positem_id = v_subtitulopost.id
		if v_descripcionpost != None:
			url = "/edit-descripcion-post/"
			positem_id = v_descripcionpost.id
		if v_codigospost != None:
			url = "/edit-codigo-post/"
			positem_id = v_codigospost.id
		if v_imagenpost != None:
			url = "/edit-imagen-post/"
			positem_id = v_imagenpost.id

		return HttpResponseRedirect(url+str(post_id)+"/"+str(postitem_id)+"/"+str(positem_id)+"/")


class DeleteItemPostView(RedirectView):

	def get(self, args, **kwargs):
		post_id = self.kwargs.get('pk1', None)
		postitem_id = self.kwargs.get('pk2', None)

		ObjPostAdd = get_object_or_404(PostAdd, pk=postitem_id)

		v_subtitulopost = ObjPostAdd.subtitulopost
		v_descripcionpost = ObjPostAdd.descripcionpost
		v_codigospost = ObjPostAdd.codigospost
		v_imagenpost = ObjPostAdd.imagenpost



		if v_subtitulopost != None:
			url = "/delete-subtitulo-post/"
			positem_id = v_subtitulopost.id
		if v_descripcionpost != None:
			url = "/delete-descripcion-post/"
			positem_id = v_descripcionpost.id
		if v_codigospost != None:
			url = "/delete-codigo-post/"
			positem_id = v_codigospost.id
		if v_imagenpost != None:
			url = "/delete-imagen-post/"
			positem_id = v_imagenpost.id

		return HttpResponseRedirect(url+str(positem_id)+"/")

class ListPostViewPost(MenuMixin,AsideMixin,GetPostSlugMixin, TemplateView):
	model = Post
	template_name = 'baseDashAngular.html'
	#Retorna los valores al template como nuevas variables
	def get_context_data(self, **kwargs):
		context = super(ListPostViewPost, self).get_context_data(**kwargs)

		ObjMenu = self.Menus()
		ObjEtiqueta = self.Etiquetas()
		ObjCategoria = self.Categorias()

		data = {
			'Categoria':ObjCategoria,
			'Etiqueta':ObjEtiqueta,
			'Menu':ObjMenu,
		}

		context.update(data)
		return context

class indexViewDashAngular(TemplateView):
	template_name = 'dashlistpost.html'