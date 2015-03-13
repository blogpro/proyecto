from django.shortcuts import render, render_to_response, get_object_or_404,render
from django.template import RequestContext

from django.views.generic import TemplateView, RedirectView, FormView

from categorias.models import Categoria
from etiquetas.models import Etiqueta

# Create your views here.

class InicioView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
		context = super(InicioView, self).get_context_data(**kwargs)
		ObjCategoria = Categoria.objects.all()
		ObjEtiqueta = Etiqueta.objects.all()
		data = {
			'Categoria':ObjCategoria,
			'Etiqueta':ObjEtiqueta,
		}

		context.update(data)
		return context	

