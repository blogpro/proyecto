from django.db import models

from etiquetas.models import Etiqueta




class Post(models.Model):
	title = models.CharField(max_length=255)
	order = models.PositiveIntegerField()
	etiquetas = models.ForeignKey(Etiqueta)
	

	def __unicode__(self):
		return self.title 


# Create your models here.
