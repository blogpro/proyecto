from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic import TemplateView, RedirectView, FormView, UpdateView, DeleteView

from post.ModelPost import GetPostMixin

#Seguridad para las vistas
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy

from post.models import Post

# Create your views here.
from menu.models import Menu

from .models import ImagenPost
from .form import ImegenForm

# Create your views here.
class LoginRequiredMixin(object): 
	@method_decorator(login_required) 
	def dispatch(self, request, *args, **kwargs): 
		return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)



class DeleteImegnPostView(DeleteView):
    model = ImagenPost
    success_url = '/access-admin-site/'
    template_name = 'deleteimagen.html'        		