from django.db import models

from django.contrib.auth.models import User
from post.models import Post

class Comentario(models.Model):
	user = models.ForeignKey(User, related_name='userperfil')
	descripcion = models.CharField(max_length=2000)
	post = models.ForeignKey(Post)
	activo = models.BooleanField(default=False)
	parent = models.ForeignKey("self",blank=True, null=True)
	fechahora = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return '%s' % (self.descripcion)

# Create your models here.
