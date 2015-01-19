from django.db import models

from post.models import Post

class Voto(models.Model):
	order = models.PositiveIntegerField()
	post = models.ForeignKey(Post)

	def __unicode__(self):
		return '%s' % (self.post)

# Create your models here.
