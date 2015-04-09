from django.shortcuts import render, render_to_response, get_object_or_404,render
from django.template import RequestContext

from django.views.generic import TemplateView, RedirectView, FormView

from menu.models import Menu
from categorias.models import Categoria
from etiquetas.models import Etiqueta
from post.models import Post,PostAdd

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

		PostMatriz = []
		for p in ObjPost:
			file_info = {}

			#----------------------------------------Lista Post---------------------------------------
			SocialArray = list()
			v_id_facebook = ""
			avatar = ""
			ObjPostAdd = PostAdd.objects.filter(post__id= p.id).order_by('order')
			for s in ObjPostAdd:
				
				SocialArray.append({
				"subtitulopost": str(s.subtitulopost),
				"descripcionpost": s.descripcionpost,
				"codigospost": str(s.codigospost),
				"imagenpost": str(s.imagenpost),
				})
			file_info['postList']=SocialArray
			#----------------------------------------Lista Post---------------------------------------
			file_info['title']=p.title
			file_info['first_name']=p.user.first_name
			file_info['last_name']=p.user.last_name
			file_info['fecha']=p.fecha_registro
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

