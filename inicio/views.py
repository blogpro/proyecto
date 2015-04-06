from django.shortcuts import render, render_to_response, get_object_or_404,render
from django.template import RequestContext

from django.views.generic import TemplateView, RedirectView, FormView

from menu.models import Menu
from categorias.models import Categoria
from etiquetas.models import Etiqueta
from post.models import Post

# Create your views here.

class InicioView(TemplateView):
    template_name = 'index.html'

    #Retorna los valores al template como nuevas variables
    def get_context_data(self, **kwargs):
		context = super(InicioView, self).get_context_data(**kwargs)
		ObjCategoria = Categoria.objects.all()
		ObjEtiqueta = Etiqueta.objects.all()
		ObjMenu = Menu.objects.all()
		ObjPost = Post.objects.all()
		data = {
			'Categoria':ObjCategoria,
			'Etiqueta':ObjEtiqueta,
			'Menu':ObjMenu,
			'Post':ObjPost,
		}

		context.update(data)
		return context	

