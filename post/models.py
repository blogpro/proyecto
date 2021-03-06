# -*- encoding: utf-8 -*-
from django.db import models

from etiquetas.models import Etiqueta
from categorias.models import Categoria
#from comentarios.models import Comentario
from votos.models import Voto

from imagenes.models import ImagenPost

from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.


class Status_Post(models.Model):
	title = models.CharField(max_length=255)
	descripcion=models.TextField()
	def __unicode__(self):
		return self.title 

from django.template import defaultfilters
class Post(models.Model):
	status = models.ForeignKey(Status_Post,blank=True, null=True)
	user = models.ForeignKey(User, related_name='perfil')
	title = models.CharField(max_length=255)
	descripcion=RichTextField()  # Usamos  RichTextField()
	etiquetas = models.ManyToManyField(Etiqueta)
	categoria = models.ForeignKey(Categoria)
	voto = models.ForeignKey(Voto,blank=True, null=True)
	date_ini = models.DateField(blank=True, null=True)
	image = models.ImageField(upload_to='images/postconfig/%Y/%m/%d', verbose_name='Imágen', blank=True, null=True)
	slug = models.SlugField()
	fecha_registro = models.DateTimeField(auto_now_add=True)

	metadescripcion = models.CharField(max_length=156)
	metakeywords = models.CharField(max_length=255,blank=True, null=True)
	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = defaultfilters.slugify(self.title)
		super(Post, self).save(*args, **kwargs)
