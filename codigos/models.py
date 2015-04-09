from django.db import models

class CodigosPost(models.Model):
	descripcion = models.TextField()
	def __unicode__(self):
		return self.descripcion 