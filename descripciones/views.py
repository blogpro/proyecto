from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic import TemplateView, RedirectView, FormView, UpdateView, DeleteView

from .models import DescripcionPost
from .form import DescripcionForm

from post.ModelPost import GetPostMixin

#Seguridad para las vistas
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy

from post.models import Post,PostAdd

# Create your views here.
from menu.models import Menu

class LoginRequiredMixin(object): 
	@method_decorator(login_required) 
	def dispatch(self, request, *args, **kwargs): 
		return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

class AddDescripcionPostView(GetPostMixin,FormView):
    template_name = 'formdescripcion.html'
    form_class = DescripcionForm

    def form_valid(self, form):
    	id_postform = self.request.POST['id_post']

    	ObjPost = Post.objects.get(pk = id_postform)

        v=form.save()
        id_descripcion = v.id
        ObjDescripcionPost = DescripcionPost.objects.get(pk=id_descripcion)

        #---------Guardamos el DescripcionPost-----------
        
        CountPostAdd = PostAdd.objects.filter(post__id=id_postform).count()
        CountPostAdd = CountPostAdd + 1

        ObjPostAdd = PostAdd()
        ObjPostAdd.post = ObjPost
        ObjPostAdd.descripcionpost = ObjDescripcionPost
        ObjPostAdd.order = CountPostAdd
        ObjPostAdd.save()
        #---------Guardamos el DescripcionPost-----------


        return HttpResponseRedirect("/add-item-post/"+id_postform+"/")
    def form_invalid(self, form):
    	return self.render_to_response(self.get_context_data(form=form))


      
    #Retorna los valores al template como nuevas variables
    def get_context_data(self, **kwargs):
		context = super(AddDescripcionPostView, self).get_context_data(**kwargs)
		ObjMenu = Menu.objects.all()

		ObjGetPost = self.GetPost(self.kwargs['pk'])

		data = {
			'Menu':ObjMenu,
			'PostMatriz':ObjGetPost,
			'id_post':self.kwargs['pk'],
		}

		context.update(data)
		return context


class EditDescripcionPostView(GetPostMixin,FormView):
    template_name = 'formdescripcion.html'
    form_class = DescripcionForm

    def form_valid(self, form):
        id_postform = self.request.POST['id_post']

        v_descripcion=self.request.POST['descripcion']

        DescripcionPost.objects.filter(pk=id_postform).update(descripcion=v_descripcion)
        ObjPostAdd=PostAdd.objects.get(descripcionpost__id=id_postform)
        post_id = str(ObjPostAdd.post.id)
        
        return HttpResponseRedirect("/add-item-post/"+post_id+"/")
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


      
    #Retorna los valores al template como nuevas variables
    def get_context_data(self, **kwargs):
        context = super(EditDescripcionPostView, self).get_context_data(**kwargs)
        ObjMenu = Menu.objects.all()

        post_id = self.kwargs['pk1']
        positem_id = self.kwargs['pk2']
        descripcion_id = self.kwargs['pk3']

        DescripcionPost_v = DescripcionPost.objects.get(pk=descripcion_id)
        DescripcionFormv = DescripcionForm(instance=DescripcionPost_v)

        #ObjGetPost = self.GetPost(post_id)

        data = {
            'Menu':ObjMenu,
            #'PostMatriz':ObjGetPost,
            'id_post':descripcion_id,
            'form':DescripcionFormv,
        }

        context.update(data)
        return context

class DeleteDescripcionPostView(DeleteView):
    model = DescripcionPost
    success_url = '/admin/'

    template_name = 'deletedescripcion.html'
