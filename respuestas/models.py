from django.db import models

from comentarios.models import Comentario

class Respuesta(models.Model):
	descripcion = models.CharField(max_length=2000)
	order = models.PositiveIntegerField()
	comentarios = models.ForeignKey(Comentario)

	def __unicode__(self):
		return '%s' % (self.comentario)

# Create your models here.
