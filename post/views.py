from django.shortcuts import render, render_to_response, get_object_or_404,render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, RedirectView, FormView, DetailView

#Seguridad para las vistas
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



from menu.models import Menu
from categorias.models import Categoria
from etiquetas.models import Etiqueta
from post.models import Post,PostAdd

from comentarios.models import Comentario


from .form import PostForm

from .ModelPost import GetPostMixin

class LoginRequiredMixin(object): 
	@method_decorator(login_required) 
	def dispatch(self, request, *args, **kwargs): 
		return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


# Create your views here.
class PostView(LoginRequiredMixin,FormView):
    template_name = 'post.html'
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
		ObjCategoria = Categoria.objects.all()
		ObjEtiqueta = Etiqueta.objects.all()
		ObjMenu = Menu.objects.all()
		ObjPost = Post.objects.all()

		ObjFormPost = PostForm()
		#Mandamos a llamar al formulario del Post

		data = {
			'Categoria':ObjCategoria,
			'Etiqueta':ObjEtiqueta,
			'Menu':ObjMenu,
			'ObjFormPost':ObjFormPost,
			'Post':ObjPost,
		}

		context.update(data)
		return context


class AddItemPostView(LoginRequiredMixin,GetPostMixin,TemplateView):
    template_name = 'additempost.html'
      
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
			url = "/edit-descripcion-post/"
			print "editar subtitulo"
		if v_descripcionpost != None:
			print "editar descripcion"
			url = "/edit-descripcion-post/"
			positem_id = v_descripcionpost.id
		if v_codigospost != None:
			print "editar codigo"
		if v_imagenpost != None:
			print "editar imagen"

		return HttpResponseRedirect(url+str(post_id)+"/"+str(postitem_id)+"/"+str(positem_id)+"/")




















class PostViewp(LoginRequiredMixin,FormView):
    template_name = 'post.html'
    form_class = PostForm
    success_url = '/post/'

    def form_valid(self, form):
        title = form.cleaned_data['title']
        form.save()
        return self.render_to_response(self.get_context_data(form=form))
    def form_invalid(self, form):
    	return self.render_to_response(self.get_context_data(form=form))    
    
    

    #Retorna los valores al template como nuevas variables
    def get_context_data(self, **kwargs):
		context = super(PostView, self).get_context_data(**kwargs)
		ObjCategoria = Categoria.objects.all()
		ObjEtiqueta = Etiqueta.objects.all()
		ObjMenu = Menu.objects.all()
		ObjPost = Post.objects.all()

		ObjFormPost = PostForm()
		#Mandamos a llamar al formulario del Post

		data = {
			'Categoria':ObjCategoria,
			'Etiqueta':ObjEtiqueta,
			'Menu':ObjMenu,
			'ObjFormPost':ObjFormPost,
			'Post':ObjPost,
		}

		context.update(data)
		return context			