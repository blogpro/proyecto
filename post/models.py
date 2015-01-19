from django.db import models

from etiquetas.models import Etiqueta

class Post(models.Model):
	title = models.CharField(max_length=255)
	descripcion = models.CharField(max_length=2000)
	order = models.PositiveIntegerField()
	post_file = models.FileField(upload_to='videos')
	post_imagen = models.ImageField(upload_to='fotos')
	etiquetas = models.ForeignKey(Etiqueta)

	def __unicode__(self):
		return self.title 


# Create your models here.
