from django.db import models


class Voto(models.Model):
	up = models.PositiveIntegerField()
	down = models.PositiveIntegerField()

	def __unicode__(self):
		return '%s' % (self.up)

# Create your models here.
