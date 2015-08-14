from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic import TemplateView, RedirectView, FormView, UpdateView, DeleteView

from post.ModelPost import GetPostMixin

#Seguridad para las vistas
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy

from post.models import Post,PostAdd

# Create your views here.
from menu.models import Menu

from .models import ImagenPost
from .form import ImegenForm

# Create your views here.
class LoginRequiredMixin(object): 
	@method_decorator(login_required) 
	def dispatch(self, request, *args, **kwargs): 
		return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

class AddImagenView(GetPostMixin,FormView):
    template_name = 'formimagen.html'
    form_class = ImegenForm

    def form_valid(self, form):
    	id_postform = self.request.POST['id_post']

    	ObjPost = Post.objects.get(pk = id_postform)

        v=form.save()
        id_ObjModel = v.id
        ObjModelPost = ImagenPost.objects.get(pk=id_ObjModel)

        #---------Guardamos el ObjModel-----------
        
        CountPostAdd = PostAdd.objects.filter(post__id=id_postform).count()
        CountPostAdd = CountPostAdd + 1

        ObjPostAdd = PostAdd()
        ObjPostAdd.post = ObjPost
        ObjPostAdd.imagenpost = ObjModelPost
        ObjPostAdd.order = CountPostAdd
        ObjPostAdd.save()
        #---------Guardamos el ObjModel-----------

        #--------------Retornamos al la lista de post general-------------
        return HttpResponseRedirect("/add-item-post/"+id_postform+"/")
        #--------------Retornamos al la lista de post general-------------
    def form_invalid(self, form):
    	return self.render_to_response(self.get_context_data(form=form))	

    #Retorna los valores al template como nuevas variables
    def get_context_data(self, **kwargs):
		context = super(AddImagenView, self).get_context_data(**kwargs)
		ObjMenu = Menu.objects.all()

		ObjGetPost = self.GetPost(self.kwargs['pk'])

		data = {
			'Menu':ObjMenu,
			'PostMatriz':ObjGetPost,
			'id_post':self.kwargs['pk'],
		}

		context.update(data)
		return context		

class EditImegenPostView(GetPostMixin,FormView):
    template_name = 'formimagen.html'
    form_class = ImegenForm

    def form_valid(self, form):
        id_postform = self.request.POST['id_post']

        v_inputform=self.request.FILES['image']
        print v_inputform



        #ImagenPost.objects.filter(pk=id_postform).update(image=v_inputform)
        form.instance.pk = id_postform
        form.instance.save()
        #self.object = form.save(commit=False)
        #self.object.save()

        ObjPostAdd=PostAdd.objects.get(codigospost__id=id_postform)
        post_id = str(ObjPostAdd.post.id)
        
        return HttpResponseRedirect("/add-item-post/"+post_id+"/")
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


      
    #Retorna los valores al template como nuevas variables
    def get_context_data(self, **kwargs):
        context = super(EditImegenPostView, self).get_context_data(**kwargs)
        ObjMenu = Menu.objects.all()

        post_id = self.kwargs['pk1']
        positem_id = self.kwargs['pk2']
        ObjModel_id = self.kwargs['pk3']

        ObjModelPost_v = ImagenPost.objects.get(pk=ObjModel_id)
        MmdelFormv = ImegenForm(instance=ObjModelPost_v)

        #ObjGetPost = self.GetPost(post_id)

        data = {
            'Menu':ObjMenu,
            #'PostMatriz':ObjGetPost,
            'id_post':ObjModel_id,
            'form':MmdelFormv,
        }

        context.update(data)
        return context


class DeleteImegnPostView(DeleteView):
    model = ImagenPost
    success_url = '/admin/'

    template_name = 'deleteimagen.html'        		