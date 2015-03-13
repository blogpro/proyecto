from django.db import models

from etiquetas.models import Etiqueta




class Post(models.Model):
	title = models.CharField(max_length=255)
	order = models.PositiveIntegerField()
	#etiquetas = models.ForeignKey(Etiqueta)
	etiquetas = models.ManyToManyField(Etiqueta, blank=True, null=True)
	

	def __unicode__(self):
		return self.title 


# Create your models here.
