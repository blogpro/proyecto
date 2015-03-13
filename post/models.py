from django.db import models

from etiquetas.models import Etiqueta
from categorias.models import Categoria
#from comentarios.models import Comentario
from votos.models import Voto




class Post(models.Model):
	title = models.CharField(max_length=255)
	order = models.PositiveIntegerField()
	#etiquetas = models.ForeignKey(Etiqueta)
	etiquetas = models.ManyToManyField(Etiqueta, blank=True, null=True)
	categoria = models.ForeignKey(Categoria)
	#comentario = models.ForeignKey(Comentario,blank=True, null=True)
	voto = models.ForeignKey(Voto,blank=True, null=True)
	

	def __unicode__(self):
		return self.title 


# Create your models here.
