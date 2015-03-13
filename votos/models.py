from django.db import models


class Voto(models.Model):
	voto = models.PositiveIntegerField()
	#post = models.ForeignKey(Post)

	def __unicode__(self):
		return '%s' % (self.voto)

# Create your models here.
