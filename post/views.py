from django.shortcuts import render, render_to_response, get_object_or_404,render
from django.views.generic import TemplateView, RedirectView, FormView

#Seguridad para las vistas
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



from menu.models import Menu
from categorias.models import Categoria
from etiquetas.models import Etiqueta

from .form import PostForm

class LoginRequiredMixin(object): 
	@method_decorator(login_required) 
	def dispatch(self, request, *args, **kwargs): 
		return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)



# Create your views here.
class PostView(LoginRequiredMixin,FormView):
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

		ObjFormPost = PostForm()

		#Mandamos a llamar al formulario del Post

		data = {
			'Categoria':ObjCategoria,
			'Etiqueta':ObjEtiqueta,
			'Menu':ObjMenu,
			'ObjFormPost':ObjFormPost,
		}

		context.update(data)
		return context	