from django.db import models

class Etiqueta(models.Model):
	title = models.CharField(max_length=255)
	order = models.PositiveIntegerField()

	def __unicode__(self):
		return self.title




# Create your models here.
