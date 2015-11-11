from django.db import models

from etiquetas.models import Etiqueta
from categorias.models import Categoria
#from comentarios.models import Comentario
from votos.models import Voto

#from subtitulos.models import SubtituloPost
from descripciones.models import DescripcionPost
from codigos.models import CodigosPost
from imagenes.models import ImagenPost

from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.


class Post(models.Model):
	user = models.ForeignKey(User, related_name='perfil')
	title = models.CharField(max_length=255)
	descripcion=RichTextField()  # Usamos  RichTextField()
	etiquetas = models.ManyToManyField(Etiqueta, blank=True, null=True)
	categoria = models.ForeignKey(Categoria)
	voto = models.ForeignKey(Voto,blank=True, null=True)
	
	fecha_registro = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.title 

class PostAdd(models.Model):
	post = models.ForeignKey(Post)
	#subtitulopost = models.ForeignKey(SubtituloPost,blank=True, null=True)
	#descripcionpost = models.ForeignKey(DescripcionPost,blank=True, null=True)
	#codigospost = models.ForeignKey(CodigosPost,blank=True, null=True)
	imagenpost = models.ForeignKey(ImagenPost,blank=True, null=True)
	
	order = models.PositiveIntegerField()
	def __unicode__(self):
		return self.post.title		


