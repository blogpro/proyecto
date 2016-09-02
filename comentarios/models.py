from django.db import models

from post.models import Post

class Comentario(models.Model):
	descripcion = models.CharField(max_length=2000)
	post = models.ForeignKey(Post)
	parent = models.ForeignKey("self",blank=True, null=True)

	def __unicode__(self):
		return '%s' % (self.descripcion)

# Create your models here.
